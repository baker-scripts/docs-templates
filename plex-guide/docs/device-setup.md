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

### Steps

1. **Plug in your Fire TV Stick** to an HDMI port on your TV and connect the power cable
2. **Turn on your TV** and select the correct HDMI input
3. **Connect to WiFi** — follow the on-screen prompts to connect to your home WiFi
4. **Open the search** — press the magnifying glass icon on your remote or say "Alexa, find Plex"
5. **Download Plex** — select "Plex" from the results and click "Download" or "Get"
6. **Open Plex** — once installed, open the app
7. **Sign in** — select "Sign in" and follow the prompts. Use the code shown on your TV at [plex.tv/link](https://plex.tv/link) on your phone or computer
8. **Find the server** — once signed in, look for **{{ server_name }}** in the left sidebar. If you don't see it, check the [troubleshooting guide](index.md#i-cant-find-{{ server_name | lower | replace(" ", "-") }}-in-the-app)

!!! tip "Quality Settings"
    For the best picture, go to **Settings > Video Quality** and set both "Home Streaming" and "Remote Streaming" to **Original** or **Maximum**. See [picture quality guide](index.md#the-picture-looks-bad-or-blurry) if video looks blurry.

{% if admin_name %}
!!! info "Need Remote Setup?"
    {{ admin_name }} can set up your Fire TV Stick remotely with additional services. Just ask!
{% endif %}

{% endif %}

{% if has_shield %}

## Setting Up Your NVIDIA Shield

### What You Need

- NVIDIA Shield TV or Shield TV Pro
- WiFi or Ethernet connection (Ethernet recommended for 4K)
- A TV with an HDMI port

### Steps

1. **Connect your Shield** to your TV via HDMI and plug in the power cable
2. **Connect to your network** — Ethernet is recommended for the best 4K experience. For WiFi, follow the on-screen setup
3. **Sign in to Google** — you need a Google account to access the Play Store
4. **Open Google Play Store** — find it on the home screen
5. **Search for "Plex"** — install the Plex app
6. **Open Plex** and sign in — use the code shown on your TV at [plex.tv/link](https://plex.tv/link) on your phone or computer
7. **Find the server** — look for **{{ server_name }}** in the left sidebar. If you don't see it, check the [troubleshooting guide](index.md#i-cant-find-{{ server_name | lower | replace(" ", "-") }}-in-the-app)

!!! tip "Quality Settings"
    The Shield supports 4K, HDR, and lossless audio. Set video quality to **Original** to get the full experience. Go to **Settings > Video Quality** and set everything to **Original** or **Maximum**.

!!! tip "Ethernet vs WiFi"
    If you're watching 4K content, use an Ethernet cable instead of WiFi. 4K streams need a stable 25+ Mbps connection, and WiFi can drop packets.

{% if admin_name %}
!!! info "Need Remote Setup?"
    {{ admin_name }} can set up your Shield remotely with additional services. Just ask!
{% endif %}

{% endif %}
