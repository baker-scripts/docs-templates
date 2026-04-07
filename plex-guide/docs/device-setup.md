---
title: Device Setup Guides
render_macros: true
---

# Device Setup Guides

Setup and usage instructions for streaming devices. For general getting started steps, see the [main guide](index.md#getting-started-one-time-setup).

[TOC]

{% if has_fire_tv %}

## Fire TV Stick

### Hardware Setup

1. Plug the Fire TV Stick into an HDMI port on your TV and connect the power cable
2. Turn on your TV and select the correct HDMI input
3. If this is a new device, follow the on-screen prompts to connect to WiFi

### Remote Button Reference

| Button | What It Does |
|--------|-------------|
| <kbd>Home</kbd> (house icon) | Go to the Fire TV home screen |
| <kbd>🔍</kbd> (magnifying glass) | Open search |
| <kbd>☰</kbd> (three lines) | Open menu / options |
| Center ring (up/down/left/right) | Navigate menus |
| Center button | Select / confirm |
| <kbd>⏯</kbd> (play/pause) | Play or pause |
| <kbd>⏪</kbd> / <kbd>⏩</kbd> (rewind/fast forward) | Skip back / forward |
| <kbd>◀</kbd> (back arrow) | Go back one screen |

!!! warning "The microphone button does not work with Plex"
    The <kbd>🎤</kbd> button on your remote is for Alexa. It cannot search, play, or control Plex. Use the on-screen search instead.

### Installing Plex

1. Press <kbd>🔍</kbd> to open search
2. Use the center ring to type **Plex** on the on-screen keyboard, then press center button to search
3. Select **Plex** from the results and press center button
4. Select **Get** or **Download** and wait for it to install

### Signing In

1. Open Plex — press <kbd>Home</kbd>, scroll to "Your Apps & Channels", select Plex
2. Select **Sign in** and note the code shown on your TV
3. On your phone or computer, go to [plex.tv/link](https://plex.tv/link) and enter the code

### Finding {{ server_name }}

1. From the Plex home screen, press the **left** direction on the center ring to open the sidebar
2. Look for **{{ server_name }}** in the list of servers
3. If you don't see it, check the [troubleshooting guide](index.md#i-cant-find-{{ server_name | lower | replace(" ", "-") }}-in-the-app)

### Navigating Plex

#### Browsing Libraries

1. Press **left** on the center ring to open the sidebar
2. Use **up/down** to switch between libraries (Movies, TV Shows, Music, etc.)
3. Press center button to enter a library
4. Use the center ring to browse through titles — **left/right** to scroll, center button to select

#### Searching for Content

1. From anywhere in Plex, press **down** on the center ring until you reach the top menu bar, then navigate to the search icon
2. Use the center ring to type on the on-screen keyboard
3. Results appear as you type — press **down** to browse results, center button to select

### Playback Controls

| Button | During Playback |
|--------|----------------|
| <kbd>⏯</kbd> | Play / pause |
| <kbd>⏪</kbd> | Skip back 10 seconds |
| <kbd>⏩</kbd> | Skip forward 30 seconds |
| **Left / right** on center ring | Scrub through the timeline |
| **Down** on center ring | Show the playback controls bar |
| **Up** on center ring | Show audio, subtitle, and quality options |
| <kbd>◀</kbd> (back) | Stop playback and return to the item page |

#### Changing Subtitles

1. During playback, press **up** on the center ring
2. Select the **subtitles** icon (speech bubble)
3. Choose the language or select **None** to turn them off
4. Press <kbd>◀</kbd> to dismiss the menu and return to playback

#### Changing Audio Track

1. During playback, press **up** on the center ring
2. Select the **audio** icon (speaker)
3. Choose the audio track (language, stereo vs surround)
4. Press <kbd>◀</kbd> to dismiss the menu and return to playback

### Quality Settings

1. From the Plex home screen, press **left** on the center ring to open the sidebar
2. Use **down** to scroll to **Settings** (gear icon) and press center button
3. Select **Video Quality**
4. Set **Home Streaming** to **Original** or **Maximum**
5. Set **Remote Streaming** to **Original** or **Maximum**
6. Press <kbd>◀</kbd> to go back

!!! tip "Still blurry?"
    See the [picture quality guide](index.md#the-picture-looks-bad-or-blurry) for more troubleshooting steps.

{% if admin_name %}
!!! info "Need Remote Setup?"
    {{ admin_name }} can set up your Fire TV Stick remotely with additional services. {{ admin_contact }}.
{% endif %}

{% endif %}

{% if has_shield %}

## NVIDIA Shield

### Hardware Setup

1. Connect the Shield to your TV via HDMI and plug in the power cable
2. Turn on your TV and select the correct HDMI input
3. If this is a new device, follow the on-screen setup — use Ethernet for the best 4K experience

### Remote Button Reference

| Button | What It Does |
|--------|-------------|
| <kbd>Home</kbd> (circle icon) | Go to the Shield home screen |
| <kbd>◀</kbd> (triangle/back) | Go back one screen |
| Touchpad (swipe up/down/left/right) | Navigate menus |
| Touchpad (click) | Select / confirm |
| <kbd>⏯</kbd> (play/pause) | Play or pause |
| Volume buttons (side) | Adjust volume |
| <kbd>☰</kbd> (menu dots) | Open options / context menu |

!!! warning "The microphone button does not work with Plex"
    The <kbd>🎤</kbd> button on your remote is for Google Assistant. It cannot search, play, or control Plex. Use the on-screen search instead.

### Installing Plex

1. Press <kbd>Home</kbd>, navigate to **Apps**, and open the **Google Play Store**
2. Select the search bar at the top and type **Plex** using the on-screen keyboard
3. Select **Plex** from the results
4. Click **Install** and wait for it to download

### Signing In

1. Open Plex — press <kbd>Home</kbd>, navigate to **Apps**, select Plex
2. Select **Sign in** and note the code shown on your TV
3. On your phone or computer, go to [plex.tv/link](https://plex.tv/link) and enter the code

### Finding {{ server_name }}

1. From the Plex home screen, swipe **left** on the touchpad to open the sidebar
2. Look for **{{ server_name }}** in the list of servers
3. If you don't see it, check the [troubleshooting guide](index.md#i-cant-find-{{ server_name | lower | replace(" ", "-") }}-in-the-app)

### Navigating Plex

#### Browsing Libraries

1. Swipe **left** on the touchpad to open the sidebar
2. Swipe **up/down** to switch between libraries (Movies, TV Shows, Music, etc.)
3. Click the touchpad to enter a library
4. Swipe to browse through titles — swipe gently to move one item, swipe and hold to scroll quickly

#### Searching for Content

1. From anywhere in Plex, swipe **down** on the touchpad until you reach the top menu bar, then navigate to the search icon
2. Click the touchpad to open search, then use the touchpad to select letters on the on-screen keyboard
3. Results appear as you type — swipe **down** to browse results, click to select

### Playback Controls

| Button | During Playback |
|--------|----------------|
| <kbd>⏯</kbd> or click touchpad | Play / pause |
| Swipe **left** on touchpad | Scrub backward through the timeline |
| Swipe **right** on touchpad | Scrub forward through the timeline |
| Swipe **down** on touchpad | Show the playback controls bar |
| Swipe **up** on touchpad | Show audio, subtitle, and quality options |
| <kbd>◀</kbd> (back) | Stop playback and return to the item page |

#### Changing Subtitles

1. During playback, swipe **up** on the touchpad
2. Select the **subtitles** icon (speech bubble)
3. Choose the language or select **None** to turn them off
4. Press <kbd>◀</kbd> to dismiss the menu and return to playback

#### Changing Audio Track

1. During playback, swipe **up** on the touchpad
2. Select the **audio** icon (speaker)
3. Choose the audio track (language, stereo vs surround)
4. Press <kbd>◀</kbd> to dismiss the menu and return to playback

### Quality Settings

1. From the Plex home screen, swipe **left** on the touchpad to open the sidebar
2. Swipe **down** to **Settings** (gear icon) and click the touchpad
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
    {{ admin_name }} can set up your Shield remotely with additional services. {{ admin_contact }}.
{% endif %}

{% endif %}
