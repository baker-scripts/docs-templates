---
render_macros: true
---

# Device Setup Guides

Quick setup instructions for the most popular streaming devices. For general getting started steps, see the [main guide](index.md#getting-started-one-time-setup).

[TOC]

{% if has_fire_tv %}

## Setting Up Your Fire TV Stick

### What You Need

- Amazon Fire TV Stick (any model — 4K Max recommended)
- WiFi connection
- A TV with an HDMI port

### Remote Control Reference

| Button | What It Does |
|--------|-------------|
| <kbd>Home</kbd> (house icon) | Go to the home screen |
| <kbd>🔍</kbd> (magnifying glass) | Open search |
| <kbd>☰</kbd> (three lines) | Open menu / options |
| <kbd>⏯</kbd> (play/pause) | Play or pause content |
| <kbd>◀</kbd> (back arrow) | Go back one screen |
| <kbd>🎤</kbd> (microphone) | Hold and speak to Alexa |
| Center ring (up/down/left/right) | Navigate menus |
| Center button | Select / confirm |

### Steps

1. **Plug in** your Fire TV Stick to an HDMI port and connect power
2. **Turn on your TV** and select the correct HDMI input
3. **Connect to WiFi** — follow the on-screen prompts
4. **Open search** — press <kbd>🔍</kbd> on your remote, or hold <kbd>🎤</kbd> and say "Plex"
5. **Download Plex** — select "Plex" from results, press <kbd>center button</kbd>, then select "Get" or "Download"
6. **Open Plex** — press <kbd>Home</kbd>, scroll to "Your Apps & Channels", select Plex
7. **Sign in** — select "Sign in", then on your phone or computer go to [plex.tv/link](https://plex.tv/link) and enter the code shown on your TV
8. **Find the server** — use <kbd>◀</kbd> to open the sidebar, look for **{{ server_name }}**. If you don't see it, check the [troubleshooting guide](index.md#i-cant-find-{{ server_name | lower | replace(" ", "-") }}-in-the-app)

### Quality Settings

1. From the Plex home screen, scroll left to open the sidebar
2. Scroll down to **Settings** (gear icon)
3. Select **Video Quality**
4. Set **Home Streaming** to **Original** or **Maximum**
5. Set **Remote Streaming** to **Original** or **Maximum**
6. Press <kbd>◀</kbd> to go back

!!! tip "Still blurry?"
    See the [picture quality guide](index.md#the-picture-looks-bad-or-blurry) for more troubleshooting steps.

{% if admin_name %}
!!! info "Need Remote Setup?"
    {{ admin_name }} can set up your Fire TV Stick remotely with additional services. Contact the server admin.
{% endif %}

{% endif %}

{% if has_shield %}

## Setting Up Your NVIDIA Shield

### What You Need

- NVIDIA Shield TV or Shield TV Pro
- WiFi or Ethernet connection (Ethernet recommended for 4K)
- A TV with an HDMI port

### Remote Control Reference

| Button | What It Does |
|--------|-------------|
| <kbd>Home</kbd> (circle icon) | Go to the home screen |
| <kbd>◀</kbd> (triangle/back) | Go back one screen |
| <kbd>⏯</kbd> (play/pause) | Play or pause content |
| <kbd>🎤</kbd> (microphone) | Hold and speak to Google Assistant |
| Center touchpad (swipe/click) | Navigate and select |
| Volume buttons (side) | Adjust volume |

### Steps

1. **Connect your Shield** to your TV via HDMI and plug in power
2. **Connect to your network** — Ethernet is recommended for 4K. For WiFi, follow the on-screen setup
3. **Sign in to Google** — you need a Google account for the Play Store
4. **Open Google Play Store** — press <kbd>Home</kbd>, scroll to "Apps", select Play Store
5. **Search for "Plex"** — use the search at the top, type or say "Plex"
6. **Install Plex** — select "Install" and wait for download
7. **Open Plex** — press <kbd>Home</kbd>, scroll to "Apps", select Plex
8. **Sign in** — select "Sign in", then on your phone or computer go to [plex.tv/link](https://plex.tv/link) and enter the code shown on your TV
9. **Find the server** — swipe left on the touchpad to open the sidebar, look for **{{ server_name }}**. If you don't see it, check the [troubleshooting guide](index.md#i-cant-find-{{ server_name | lower | replace(" ", "-") }}-in-the-app)

### Quality Settings

1. From the Plex home screen, swipe left to open the sidebar
2. Scroll down to **Settings** (gear icon)
3. Select **Video Quality**
4. Set **Home Streaming** to **Original**
5. Set **Remote Streaming** to **Original**
6. Press <kbd>◀</kbd> to go back

!!! tip "4K + Lossless Audio"
    The Shield supports 4K, HDR, Dolby Vision, and lossless audio (TrueHD/Atmos). Set quality to **Original** to get the full experience.

!!! tip "Ethernet vs WiFi"
    Use an Ethernet cable instead of WiFi for 4K content. 4K streams need a stable 25+ Mbps connection, and WiFi can drop packets.

{% if admin_name %}
!!! info "Need Remote Setup?"
    {{ admin_name }} can set up your Shield remotely with additional services. Contact the server admin.
{% endif %}

{% endif %}
