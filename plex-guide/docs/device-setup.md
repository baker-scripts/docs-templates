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

## Apple TV

### Installing Plex

1. From the Apple TV home screen, open the **App Store**
2. Search for **Plex** and select it from the results
3. Tap **Get** and wait for the download to complete

### Signing In

1. Open Plex and select **Sign In**
2. The app shows a code on your TV screen — on your phone or computer, go to [plex.tv/link](https://plex.tv/link) and enter the code
3. Once linked, your account is active on the Apple TV immediately

### Finding {{ server_name }}

1. From the Plex home screen, press the **back/menu button** (or swipe right on older remotes) to open the sidebar
2. Look for **{{ server_name }}** under "Other Servers" or in the server list
3. If you don't see it, check the [troubleshooting guide](index.md#i-cant-find-{{ server_name | lower | replace(" ", "-") }}-in-the-app)

### Playback Controls

| Action | Siri Remote Gesture |
|--------|-------------------|
| Play / pause | Press the <kbd>⏯</kbd> button or click the touchpad |
| Skip forward 10 seconds | Swipe right on the touchpad |
| Skip back 10 seconds | Swipe left on the touchpad |
| Fast-forward / rewind | Hold the swipe |
| Open subtitles / audio menu | Swipe down on the touchpad during playback |
| Go back to the item page | Press <kbd>Back / Menu</kbd> |

### Quality Settings

1. From the Plex sidebar, scroll down to **Settings** and press the touchpad
2. Select **Video Quality**
3. Set **Remote Streaming** to **Original** or **Maximum**
4. Press <kbd>Back</kbd> to save

!!! tip "Direct Play on Apple TV 4K"
    The Apple TV 4K plays most files natively (H.264, H.265, HDR10, Dolby Vision) without transcoding. Setting quality to **Original** prevents any quality loss.

---

## Roku

### Installing Plex

1. From the Roku home screen, scroll to **Streaming Channels** and open the **Channel Store**
2. Search for **Plex** using the on-screen keyboard
3. Select **Plex** and choose **Add Channel** — it installs in a few seconds

### Signing In

1. Open Plex from the Roku home screen
2. Select **Sign In** — the app displays a short code on your TV
3. On your phone or computer, go to [plex.tv/link](https://plex.tv/link) and enter the code

### Finding {{ server_name }}

1. From the Plex home screen, press the **left arrow** on the remote to open the sidebar
2. Scroll down to find **{{ server_name }}** under the server list
3. If you don't see it, check the [troubleshooting guide](index.md#i-cant-find-{{ server_name | lower | replace(" ", "-") }}-in-the-app)

### Playback Controls

| Button | During Playback |
|--------|----------------|
| <kbd>OK</kbd> | Play / pause |
| <kbd>◀</kbd> (rewind) | Skip back 10 seconds |
| <kbd>▶</kbd> (fast-forward) | Skip forward 30 seconds |
| **Left / right** directional pad | Scrub through the timeline |
| **Down** directional pad | Show audio, subtitle, and quality options |
| <kbd>Back</kbd> | Stop and return to the item page |

### Quality Settings

1. On the Plex home screen, press the **left arrow** to open the sidebar
2. Scroll down to **Settings** (gear icon)
3. Select **Video Quality**
4. Set both **Home Streaming** and **Remote Streaming** to **Original** or **Maximum**

!!! warning "Roku and Lossless Audio"
    Roku devices do not support lossless audio formats (TrueHD, Atmos). Plex will transcode the audio track to stereo automatically — video quality is unaffected.

---

## Smart TVs (Samsung / LG / Vizio) — not recommended

!!! danger "Smart TV apps are the worst way to watch {{ server_name }}"
    Built-in TV Plex apps are the lowest-quality, least-reliable option for streaming. We strongly recommend a dedicated streaming device instead. Reasons:

    - **Missing features** — Smart TV apps lag the official Plex roadmap by years. Dolby Vision, lossless audio passthrough, and high-quality subtitle rendering are missing or broken on most models.
    - **Forced transcoding** — Most TV apps cannot direct-play higher-bitrate or non-standard codecs. The server transcodes on the fly, which spikes server CPU and degrades picture quality (banding, softness, lost HDR metadata).
    - **Broken audio passthrough** — DTS-HD MA and TrueHD are typically downmixed to PCM, and Atmos is lost entirely. You will not get the soundtrack the file actually contains.
    - **Poor app stability** — Frequent freezes, slow library loads, and Plex apps that get abandoned by the TV manufacturer 1–2 years after the model ships.

    **Use one of these instead** (already documented above): [Apple TV](#apple-tv) (best — direct plays nearly everything, full Atmos, Dolby Vision), [NVIDIA Shield](#nvidia-shield), or [Fire TV Stick](#fire-tv-stick).

If you must use the TV's built-in app, instructions for each platform follow.

### Samsung TV (Tizen)

!!! warning "Tizen apps are short-lived"
    Samsung typically drops Plex app support 1–2 years after a TV model ships. If your TV is more than 2 years old, expect the Plex app to either be missing from the store or stuck on an old version that no longer connects to current servers.

#### Installing Plex

1. Open the **Smart Hub** and navigate to **Apps**
2. Search for **Plex** and install it

Most 2017 and newer Samsung TVs support the Plex app directly from the built-in store.

#### Signing In

1. Open Plex on your TV and select **Sign In**
2. Note the code displayed on screen, then go to [plex.tv/link](https://plex.tv/link) on your phone or computer and enter the code
3. Your account links immediately — no password typing on the TV required

#### Finding {{ server_name }}

1. After signing in, press the **left** or **back** button on your remote to open the Plex sidebar
2. Scroll down until you see **{{ server_name }}** in the server list
3. If it doesn't appear, sign out and back in — check the [troubleshooting guide](index.md#i-cant-find-{{ server_name | lower | replace(" ", "-") }}-in-the-app)

#### Playback Controls

Use the **directional pad** on your TV remote — Plex shows on-screen icons when you press the down arrow or OK button during playback. Subtitles and audio track selection live in the same on-screen menu.

### LG TV (webOS)

!!! warning "webOS lossless audio is broken"
    LG webOS 5.0+ has a long-standing bug where lossless audio tracks (TrueHD / DTS-HD MA) are silently downmixed to stereo PCM, even when the TV is connected to an Atmos-capable receiver. There is no fix on LG's side — use an Apple TV or Shield in front of the TV if audio matters to you.

#### Installing Plex

1. Open the **LG Content Store**
2. Search for **Plex** and install it

Most 2017 and newer LG TVs support the Plex app from the built-in store.

#### Signing In

1. Open Plex and select **Sign In**
2. On your phone or computer, go to [plex.tv/link](https://plex.tv/link) and enter the code shown on screen

#### Finding {{ server_name }}

1. Press the **left** or **back** button on the Magic Remote to open the Plex sidebar
2. Scroll until you see **{{ server_name }}** in the server list
3. If it doesn't appear, see the [troubleshooting guide](index.md#i-cant-find-{{ server_name | lower | replace(" ", "-") }}-in-the-app)

#### Playback Controls

Point the Magic Remote at the screen and click to interact, or use the directional ring. Audio and subtitle menus appear when you press **down** or **OK** during playback.

### Vizio TV (SmartCast)

!!! warning "Vizio has no native Plex app on most models"
    Most Vizio SmartCast TVs (2016–present) **do not include a native Plex app**. The "Plex" tile on the home screen is a Chromecast Built-in target — you cast to it from the Plex mobile or web app, which forces the server to transcode every stream. This is the worst-case path: poor picture quality, no Atmos passthrough, and your phone has to stay connected.

#### How it actually works

1. On your phone, open Plex and sign in
2. Start playing something from **{{ server_name }}**
3. Tap the <kbd>cast</kbd> icon and pick your Vizio TV
4. Playback runs through Chromecast on the TV — your phone is the remote

#### Limitations to expect

- **No Atmos / lossless audio** — Chromecast on Vizio downmixes to stereo or 5.1 PCM
- **Forced transcoding** — Anything above ~20 Mbps or in a non-standard codec is transcoded by the server, lowering quality
- **No HDR / Dolby Vision on most models** — Even Vizio's "P-Series" with native DV doesn't get DV through the cast path
- **Phone-tethered** — Closing Plex on your phone or losing WiFi stops playback

#### Newer Vizio models (2022+ with built-in Plex)

A small number of newer Vizio models ship with a real Plex app under **Apps → Plex**. If yours has one, install and sign in the same way as Samsung/LG above — but the [smart TV caveats at the top of this section](#smart-tvs-samsung--lg--vizio--not-recommended) still apply.

### Better alternatives for your TV screen

!!! tip "Plug a real streaming device into the same TV"
    Any of these will give you a dramatically better experience than a Smart TV app, and they all plug into a spare HDMI port:

    - **[Apple TV 4K](#apple-tv)** — best overall. Direct plays nearly every file, full Atmos and Dolby Vision passthrough, fastest UI. ~$130.
    - **[NVIDIA Shield](#nvidia-shield)** — best for tinkerers and 4K HDR with Ethernet. Full lossless audio, AI upscaling. ~$200.
    - **[Fire TV Stick 4K Max](#fire-tv-stick)** — cheapest path to a competent Plex experience. ~$60.

    See [Recommended Streaming Devices](index.md#recommended-streaming-devices) for {{ admin_name | default("the admin") }}'s current pick.

---

## Mobile Apps (iOS and Android)

### Plex App

The Plex app is the main way to watch {{ server_name }} on your phone or tablet.

- **iPhone / iPad:** [Download from the App Store](https://apps.apple.com/app/plex/id383457673)
- **Android:** [Download from Google Play](https://play.google.com/store/apps/details?id=com.plexapp.android)

After installing, open the app, tap **Sign In**, and enter your Plex email and password. Tap {{ server_name }} on the left to start browsing.

!!! note "One-Time Unlock Fee"
    The Plex mobile app has a $5 one-time unlock fee to watch video. To skip this fee, watch via your phone's browser at [app.plex.tv](https://app.plex.tv) instead, or get [Plex Pass](https://www.plex.tv/plex-pass/) which includes the unlock.

### Plexamp (Music)

Plexamp is a dedicated music player for Plex — it streams your music library with a clean interface and gapless playback.

- **iPhone / iPad:** [Download from the App Store](https://apps.apple.com/app/plexamp/id1500797510)
- **Android:** [Download from Google Play](https://play.google.com/store/apps/details?id=tv.plex.labs.plexamp)

Sign in with the same Plex account and select {{ server_name }} as your server. Plexamp works best for music libraries — use the main Plex app for movies and TV shows.

!!! note "Plexamp Premium Features"
    Some Plexamp features (offline sync, crossfade, lyrics) require a [Plex Pass](https://www.plex.tv/plex-pass/). Basic streaming works without it.

---

## Web Browser

The Plex web player works in any modern browser — no download required.

1. Go to [app.plex.tv](https://app.plex.tv) and sign in with your Plex email and password
2. Select **{{ server_name }}** from the left sidebar
3. Browse and play content directly in your browser

**Tip:** Bookmark [app.plex.tv](https://app.plex.tv) for quick access — or use [{{ media_url }}](https://{{ media_url }}) if your admin set up a direct link.

!!! note "Browser Limitations"
    The web player does not support 4K, HDR, or lossless audio — these require a native app or dedicated device. Most HD content plays without issues.

!!! tip "Free Streaming"
    The browser player is always free and does not require the $5 mobile unlock fee or a Plex Pass subscription. If you're on a phone or tablet, open your browser and go to [app.plex.tv](https://app.plex.tv) to watch without any fees.
