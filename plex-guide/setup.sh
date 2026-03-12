#!/bin/bash
# shellcheck disable=SC2154
# Variables are dynamically assigned by prompt/prompt_bool via eval
set -euo pipefail

# Interactive setup script for Plex Guide template
# Prompts for server details, updates mkdocs.yml, and builds static HTML

readonly SAMPLE_FILE="mkdocs.sample.yml"
readonly CONFIG_FILE="mkdocs.yml"
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly CYAN='\033[0;36m'
readonly NC='\033[0m'

print_header() {
  printf "\n%b%s%b\n" "$CYAN" "================================================" "$NC"
  printf "%b  Plex Guide Template Setup%b\n" "$CYAN" "$NC"
  printf "%b%s%b\n\n" "$CYAN" "================================================" "$NC"
}

prompt() {
  local var_name="$1"
  local prompt_text="$2"
  local default="${3:-}"
  local value

  if [[ -n "$default" ]]; then
    printf "%b%s%b [%s]: " "$GREEN" "$prompt_text" "$NC" "$default"
  else
    printf "%b%s%b: " "$GREEN" "$prompt_text" "$NC"
  fi

  IFS= read -r value
  if [[ -z "$value" ]]; then
    value="$default"
  fi

  eval "$var_name=\"\$value\""
}

prompt_bool() {
  local var_name="$1"
  local prompt_text="$2"
  local default="${3:-false}"
  local display_default
  local value

  if [[ "$default" == "true" ]]; then
    display_default="Y/n"
  else
    display_default="y/N"
  fi

  printf "%b%s%b [%s]: " "$GREEN" "$prompt_text" "$NC" "$display_default"
  IFS= read -r value

  if [[ -z "$value" ]]; then
    eval "$var_name=$default"
  elif [[ "$value" =~ ^[Yy] ]]; then
    eval "$var_name=true"
  else
    eval "$var_name=false"
  fi
}

update_config() {
  local key="$1"
  local value="$2"
  local is_bool="${3:-false}"

  if [[ "$is_bool" == "true" ]]; then
    sed -i "s|^\(  ${key}:\).*|\1 ${value}|" "$CONFIG_FILE"
  else
    sed -i "s|^\(  ${key}:\).*|\1 \"${value}\"|" "$CONFIG_FILE"
  fi
}

print_header

if [[ ! -f "$SAMPLE_FILE" ]]; then
  printf "Error: %s not found. Run this script from the plex-guide directory.\n" "$SAMPLE_FILE" >&2
  exit 1
fi

# Copy sample to working config (gitignored)
cp "$SAMPLE_FILE" "$CONFIG_FILE"
printf "Created %s from %s\n\n" "$CONFIG_FILE" "$SAMPLE_FILE"

printf "This script will configure your Plex guide with your server's details.\n"
printf "Press Enter to accept defaults shown in brackets.\n\n"

# Required settings
printf "%b=== Server Details ===%b\n\n" "$YELLOW" "$NC"
prompt server_name "Server name" "My Plex Server"
prompt admin_name "Admin name (first name)" "Admin"
prompt admin_contact "How should users contact you" "Message ${admin_name}"
prompt media_url "Plex access URL (without https://)" "app.plex.tv"

# Optional features
printf "\n%b=== Optional Features ===%b\n\n" "$YELLOW" "$NC"

prompt_bool has_request_system "Do you run Overseerr/Jellyseerr?" "false"
request_url=""
if [[ "$has_request_system" == "true" ]]; then
  prompt request_url "Request system URL (without https://)" "requests.example.com"
fi

prompt_bool has_discord "Do you have a Discord server?" "false"
discord_url=""
if [[ "$has_discord" == "true" ]]; then
  prompt discord_url "Discord invite URL" "https://discord.gg/example"
fi

prompt_bool has_newsletter "Do you use Tautulli newsletters?" "false"
newsletter_url=""
if [[ "$has_newsletter" == "true" ]]; then
  prompt newsletter_url "Newsletter URL" ""
fi

prompt_bool has_guide_url "Will you host this guide publicly?" "false"
guide_url=""
if [[ "$has_guide_url" == "true" ]]; then
  prompt guide_url "Public guide URL (without https://)" ""
fi

prompt_bool has_plex_pass "Does your server have a Plex Pass?" "true"
prompt_bool has_plex_home "Do you use Plex Home for some users?" "false"
prompt_bool has_migration "Do you offer watch history migration?" "false"

prompt_bool show_costs "Show server cost information?" "false"
server_cost=""
if [[ "$show_costs" == "true" ]]; then
  prompt server_cost "Monthly server cost" "~\$50/month"
fi

# Update config
printf "\n%bUpdating %s...%b\n" "$YELLOW" "$CONFIG_FILE" "$NC"

# Update site_name and site_author
sed -i "s|^site_name:.*|site_name: ${server_name} Guide|" "$CONFIG_FILE"
sed -i "s|^site_author:.*|site_author: ${admin_name}|" "$CONFIG_FILE"

# Update extra: variables
update_config "server_name" "$server_name"
update_config "admin_name" "$admin_name"
update_config "admin_contact" "$admin_contact"
update_config "media_url" "$media_url"
update_config "has_request_system" "$has_request_system" true
update_config "request_url" "$request_url"
update_config "has_discord" "$has_discord" true
update_config "discord_url" "$discord_url"
update_config "has_newsletter" "$has_newsletter" true
update_config "newsletter_url" "$newsletter_url"
update_config "has_guide_url" "$has_guide_url" true
update_config "guide_url" "$guide_url"
update_config "has_plex_pass" "$has_plex_pass" true
update_config "has_plex_home" "$has_plex_home" true
update_config "has_migration" "$has_migration" true
update_config "show_costs" "$show_costs" true
update_config "server_cost" "$server_cost"

printf "%bConfiguration updated.%b\n\n" "$GREEN" "$NC"

# Build
printf "%b=== Build Options ===%b\n\n" "$YELLOW" "$NC"
printf "1) Build static HTML (recommended for hosting)\n"
printf "2) Start live preview server\n"
printf "3) Skip build (configure only)\n\n"
printf "%bChoose an option%b [1]: " "$GREEN" "$NC"
IFS= read -r build_choice
build_choice="${build_choice:-1}"

if ! command -v pip >/dev/null 2>&1; then
  printf "\n%bPython/pip not found. Install Python 3 first:%b\n" "$YELLOW" "$NC"
  printf "  https://www.python.org/downloads/\n\n"
  exit 1
fi

# Install deps if needed
if ! command -v mkdocs >/dev/null 2>&1; then
  printf "\nInstalling MkDocs and plugins...\n"
  pip install -r requirements.txt
fi

case "$build_choice" in
  1)
    printf "\nBuilding static HTML...\n"
    mkdocs build
    printf "\n%bDone! Static site generated in site/ directory.%b\n" "$GREEN" "$NC"
    printf "You can serve it with any web server, upload to GitHub Pages, etc.\n"
    ;;
  2)
    printf "\nStarting preview server at http://localhost:8000...\n"
    printf "Press Ctrl+C to stop.\n\n"
    mkdocs serve
    ;;
  3)
    printf "\n%bConfiguration complete.%b Run 'mkdocs build' or 'mkdocs serve' when ready.\n" "$GREEN" "$NC"
    ;;
  *)
    printf "\nUnknown option. Run 'mkdocs build' or 'mkdocs serve' manually.\n"
    ;;
esac
