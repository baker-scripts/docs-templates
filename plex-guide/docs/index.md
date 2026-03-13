---
title: "{{ server_name }} Streaming"
description: "Watch movies and TV shows on {{ server_name }}"
render_macros: true
tags:
  - plex
  - media
  - streaming
---

# {{ server_name }}

{% if has_guide_url %}
!!! tip "Quick link: [{{ guide_url }}](https://{{ guide_url }})"
{% endif %}

{{ server_tagline | default("Your personal streaming service — movies, TV shows, and more.") }}

[TOC]

## Quick Links

<!-- markdownlint-disable MD055 MD056 -->
| Action | Link |
|--------|------|
| **Watch Now** | [{{ media_url }}](https://{{ media_url }}) |
{% if has_request_system %}| **Request Something** | [{{ request_url }}](https://{{ request_url }}) |
{% endif %}{% if has_discord %}| **Get Notifications** | [Discord]({{ discord_url }}) |
{% endif %}{% if has_newsletter %}| **Weekly Newsletter** | [What's New]({{ newsletter_url }}) |
{% endif %}| **Plex Help Center** | [support.plex.tv](https://support.plex.tv/articles/) |
<!-- markdownlint-enable MD055 MD056 -->

---

## Having Issues?

??? warning "Click here if something isn't working"

    **Can't find {{ server_name }}?**

    → Check your email for an invite from Plex and click **Accept**

    → Sign out and back in ([how to sign out](https://support.plex.tv/articles/201862428-plex-accounts/))

    **Video keeps freezing?**

    → Lower the quality (see [Troubleshooting](#video-keeps-stopping-or-buffering) below)

    → Restart the Plex app

    **Forgot your password?**

    → [Reset it here](https://www.plex.tv/sign-in/)

    **Something else?**

    → Check [Plex Support](https://support.plex.tv/articles/) or scroll to [Troubleshooting](#troubleshooting)

---

## Getting Started (One-Time Setup)

### Step 1: Create Your Free Account

1. Go to [plex.tv/sign-up](https://www.plex.tv/sign-up/)
2. Enter your **email** and pick a **password**
3. Check your email and click the confirmation link
4. **{{ admin_contact }} your email address** so they can give you access

!!! warning "One-Time Requirement"
    {{ admin_name }} needs to add your email before {{ server_name }} appears. This only needs to happen once.

### Step 2: Get the Plex App

| Device | What to Do |
|--------|------------|
| **Smart TV** (Samsung, LG, etc.) | Open your TV's app store, search "Plex", install it |
| **Roku** | Go to Streaming Channels → search "Plex" → add it |
| **Fire TV Stick** | Go to Search → type "Plex" → download it |
| **Apple TV** | Open App Store → search "Plex" → download it |
| **iPhone/iPad** | [Get it from the App Store](https://apps.apple.com/app/plex/id383457673) |
| **Android** | [Get it from Google Play](https://play.google.com/store/apps/details?id=com.plexapp.android) |
| **Computer** | Just go to [app.plex.tv](https://app.plex.tv) - no download needed |

For more device setup help, see [Plex's official app guide](https://support.plex.tv/articles/categories/player-apps-platforms/).

### Step 3: Sign In and Watch

1. Open the Plex app
2. Tap **Sign In**
3. Enter your email and password
4. Look for **{{ server_name }}** on the left side
5. Start watching!

!!! tip "Can't Find {{ server_name }}?"
    1. Check your email for an invitation from Plex - click "Accept"
    2. Sign out and back in (see [how to sign out](https://support.plex.tv/articles/201862428-plex-accounts/))
    3. If you never got an invite, confirm {{ admin_name }} has your correct email

---

{% if has_request_system %}

## Requesting Movies and Shows

Can't find something? Request it!

### How to Request

1. Go to [{{ request_url }}](https://{{ request_url }})
2. Sign in with your Plex email and password
3. Search for what you want
4. Click on it and hit **Request**

Requests are processed automatically - most content appears within a day.

!!! tip "Request Tips"
    - **Same name, different movie?** Check the year to pick the right one
    - **TV shows**: You can request a whole series or just certain seasons
    - **Brand new movies**: If it's still in theaters, it won't be available yet

### Something Wrong With a Movie?

If the sound is off, subtitles are missing, or video looks bad:

1. Go to [{{ request_url }}](https://{{ request_url }})
2. Search for the movie/show with the problem
3. Click on it
4. Click **Report Issue**
5. Describe what's wrong

---
{% endif %}

## Do I Need to Pay?

{% if show_costs %}
**Access is free**, but the server costs {{ server_cost }} plus significant time to manage. If you'd like to contribute, reach out to {{ admin_name }} - any contribution is appreciated but never required.
{% else %}
**Access is free.** If you'd like to contribute toward server costs, reach out to {{ admin_name }} - any contribution is appreciated but never required.
{% endif %}

{% if has_plex_pass %}

### Plex Pass - What You Get

The server has a [Plex Pass](https://www.plex.tv/plex-pass/) subscription. **You don't need to buy Plex Pass yourself** to watch content.

Because this server has Plex Pass, you can stream remotely on any device — TV, phone, tablet, or computer — at no cost.

The server's Plex Pass automatically benefits **all users**:

- **Hardware-accelerated streaming** - Videos start faster and play more smoothly
- **HDR tone mapping** - HDR content looks correct even on non-HDR screens
- **Remote streaming** - Watch from anywhere on any device

{% if has_plex_home %}
!!! note "Plex Home Members"
    A few users are part of the **Plex Home** and automatically get Skip Intro/Credits, Lyrics, and Trailers. If you're not sure whether you're in Plex Home, you probably aren't — ask {{ admin_name }}.
{% endif %}

### Get Your Own Plex Pass (Optional)

A personal [Plex Pass](https://www.plex.tv/plex-pass/) ($6.99/month, $69.99/year, or $249.99 lifetime) gives you features the server can't provide:

<!-- markdownlint-disable MD055 MD056 -->
| Feature | Description |
|---------|-------------|
{% if has_plex_home %}| **Skip Intro/Credits** | If you're not in Plex Home, get this feature with your own pass |
{% else %}| **Skip Intro/Credits** | Automatically skip TV show intros and credits |
{% endif %}| **Mobile Downloads** | Download movies/shows to watch offline (planes, road trips, etc.) |
| **Lyrics** | See song lyrics while listening to music |
| **Free Mobile App** | No $5 unlock fee for iPhone/Android apps |
| **Early Access** | Try new Plex features before everyone else |
| **Plexamp Premium** | Enhanced music player features |
<!-- markdownlint-enable MD055 MD056 -->

Compare all options at [plex.tv/plans](https://www.plex.tv/plans/).

!!! tip "Is Plex Pass Worth It?"
    **Most users: yes.** The $249.99 lifetime pass pays for itself quickly. You get Skip Intro/Credits on every show, offline downloads for travel, and free mobile apps. The $69.99/year option is good if you want to try it first.

!!! note "Phone/Tablet App Without Plex Pass"
    The Plex mobile app has a one-time $5 unlock fee. To avoid this:

    - Watch on your **TV** instead (free)
    - Use [{{ media_url }}](https://{{ media_url }}) in your phone's browser (free)

{% else %}

### Remote Streaming — What You Need

Since late 2025, Plex requires a paid plan to stream remotely on TV and mobile apps. **Streaming via a computer browser is still free.**

<!-- markdownlint-disable MD055 MD056 -->
| Plan | Price | What You Get |
|------|-------|-------------|
| **Remote Watch Pass** | $2.99/month or $29.99/year | Remote streaming on TV and mobile apps |
| **Plex Pass** | $6.99/month, $69.99/year, or $249.99 lifetime | Remote streaming + Skip Intro/Credits, Downloads, Lyrics, Free Mobile App, and more |
<!-- markdownlint-enable MD055 MD056 -->

Compare all options at [plex.tv/plans](https://www.plex.tv/plans/).

!!! tip "Which Plan Should I Get?"
    If you only watch on your **computer browser**, you don't need either plan. If you watch on a **TV, phone, or tablet**, the **Remote Watch Pass** ($2.99/month) is the minimum. **Plex Pass** adds Skip Intro/Credits, offline downloads, and other features — the $249.99 lifetime option pays for itself quickly.

!!! note "Phone/Tablet App Without Plex Pass"
    The Plex mobile app has a one-time $5 unlock fee. To avoid this:

    - Watch on your **TV** instead (free with Remote Watch Pass)
    - Use [{{ media_url }}](https://{{ media_url }}) in your phone's browser (free)
{% endif %}

---

## Troubleshooting

### Video Keeps Stopping or Buffering

**What's happening:** The spinning circle keeps appearing, or the video freezes.

This is almost always an internet speed issue. Plex needs a stable connection to stream smoothly.

=== "On Your TV"

    **Step 1: Lower the video quality**

    1. While the video is playing, press the **down arrow** on your remote
    2. Look for a **gear icon** (settings) or **"Quality"**
    3. Select it and choose **"720p"** or **"2 Mbps"**
    4. This uses less internet and stops the freezing

    **Step 2: Restart the Plex app**

    1. Press the **Home** button on your remote
    2. Go back into the Plex app
    3. Try playing your video again

    **Step 3: Restart your TV**

    1. Unplug your TV from the wall
    2. Wait 30 seconds
    3. Plug it back in and turn it on
    4. Open Plex and try again

=== "On Your Phone/Tablet"

    **Step 1: Lower the video quality**

    1. While watching, tap the screen once
    2. Tap the **three dots** (...) or **gear icon**
    3. Tap **"Quality"**
    4. Choose **"720p 2Mbps"** or lower

    **Step 2: Close and reopen the app**

    - **iPhone/iPad:** Swipe up from the bottom and swipe Plex away, then reopen
    - **Android:** Tap the square button, swipe Plex away, then reopen

=== "On Your Computer"

    1. Click the **gear icon** in the bottom-right while watching
    2. Click **"Quality"**
    3. Choose **"720p 2Mbps"** or **"Convert automatically"**

**Still buffering?** Try these:

- Move closer to your WiFi router
- Plug your TV into the router with an ethernet cable
- Test your internet speed at [{{ speedtest_url | default("fast.com") }}](https://{{ speedtest_url | default("fast.com") }}) - you need at least 10 Mbps for HD

For more help: [Plex Playback Quality Guide](https://support.plex.tv/articles/quality-suggestions/)

---

### I Can't Find {{ server_name }} in the App

**What's happening:** You open Plex but don't see "{{ server_name }}" on the left side.

#### Step 1: Check your email for an invitation

1. Open your email app
2. Search for emails from **"Plex"**
3. Look for one that says **"You've been invited"** or **"shared a library"**
4. Open it and click the big **"Accept"** button

#### Step 2: Sign out and back in

=== "On Your TV"

    1. Open Plex
    2. Go to **Settings** (gear icon, usually on the left)
    3. Scroll down to find **"Sign Out"**
    4. Sign out
    5. Sign back in with your email and password

=== "On Your Phone/Tablet"

    1. Open Plex
    2. Tap your **profile picture** (top-left corner)
    3. Tap **"Sign Out"**
    4. Sign back in

=== "On Your Computer"

    1. Go to [app.plex.tv](https://app.plex.tv)
    2. Click your profile picture (top-right)
    3. Click **"Sign Out"**
    4. Sign back in

**Still not seeing it?** Make sure {{ admin_name }} has your correct email address on file.

For more help: [Plex Account Help](https://support.plex.tv/articles/201862428-plex-accounts/)

---

### I Forgot My Password

1. Go to [plex.tv/sign-in](https://www.plex.tv/sign-in/)
2. Click **"Forgot?"** next to the password field
3. Enter your email address
4. Check your email for a reset link (check spam folder too)
5. Click the link and create a new password

For more help: [Plex Password Reset Guide](https://support.plex.tv/articles/account-requires-password-reset/)

---

??? note "The Video Has No Sound"

    === "On Your TV"

        1. Make sure your TV isn't muted (press volume up on remote)
        2. While playing the video, press **down arrow** on your remote
        3. Look for **"Audio"** and select it
        4. Try a different audio track - pick one that says "English" or "Stereo"
        5. Avoid tracks labeled "TrueHD" or "Atmos" if you don't have a soundbar

    === "On Your Phone/Tablet"

        1. Make sure your phone isn't on silent mode
        2. Turn your volume up
        3. Tap the screen, then tap the **settings icon** (gear or three dots)
        4. Select **Audio** and pick a different audio track

    **Still no sound?** Try a different movie to see if it's just that one file. For more help: [Plex Audio Troubleshooting](https://support.plex.tv/articles/200430313-troubleshooting/)

??? note "I Want Subtitles (Captions)"

    === "On Your TV"

        1. While the video is playing, press the **down arrow** on your remote
        2. Look for **"Subtitles"** or the **subtitle icon** (box with horizontal lines)
        3. Select it
        4. Choose **"English"** or your preferred language

    === "On Your Phone/Tablet"

        1. Tap the screen while watching
        2. Tap the **settings icon** (gear or three dots, usually bottom-right)
        3. Tap **Subtitles** and pick **"English"**

    === "On Computer"

        1. While watching, move your mouse to show controls
        2. Click the **subtitle icon** (box with horizontal lines, or "CC")
        3. Select your subtitle language

    {% if has_request_system %}
    **No subtitles available?** Not all videos have subtitles. You can report the issue at [{{ request_url }}](https://{{ request_url }}).
    {% else %}
    **No subtitles available?** Not all videos have subtitles. Contact {{ admin_name }} to report the issue.
    {% endif %}

    For more help: [Plex Subtitle Guide](https://support.plex.tv/articles/subtitle-search/)

??? note "The Movie is in a Foreign Language"

    The audio track might be set to another language by default.

    1. While watching, look for **"Audio"** settings (press down arrow on TV, or tap gear icon on phone)
    2. Change it from the foreign language to **"English"**

    {% if has_request_system %}
    **If there's no English option:** That movie might only be available in the original language. Report it at [{{ request_url }}](https://{{ request_url }}).
    {% else %}
    **If there's no English option:** That movie might only be available in the original language. Contact {{ admin_name }} to report the issue.
    {% endif %}

??? note "The Picture Looks Bad or Blurry"

    This usually means the quality got lowered to prevent buffering.

    === "On Your TV"

        1. While watching, press the **down arrow**
        2. Find **"Quality"**
        3. Choose **"Original"** or **"Maximum"**

    === "On Your Phone/Tablet"

        1. Tap the screen
        2. Tap the **gear icon** or **three dots**
        3. Tap **"Quality"**
        4. Choose the highest option

    **Still blurry?** Your internet might be too slow for HD. Try:

    - Moving closer to your WiFi router
    - Plugging your TV into the router with a cable
    - Testing your speed at [{{ speedtest_url | default("fast.com") }}](https://{{ speedtest_url | default("fast.com") }}) - you need 25+ Mbps for 4K

    For more help: [Plex Quality Settings](https://support.plex.tv/articles/quality-suggestions/)

??? note "App Crashes or Won't Open"

    1. **Update the app** - Go to your device's app store and check for Plex updates
    2. **Restart your device** - Turn it off and back on
    3. **Reinstall Plex** - Delete the app and install it fresh from the app store

    For device-specific help: [Plex App Troubleshooting](https://support.plex.tv/articles/categories/player-apps-platforms/)

---

### {{ server_name }} Won't Load At All

**What's happening:** [{{ media_url }}](https://{{ media_url }}) shows an error or won't load, and the Plex app says "Server unavailable."

This means the server might be down. **{{ admin_contact }}** - this is something only they can fix.

Before contacting them, try:

1. Try opening [{{ media_url }}](https://{{ media_url }}) — if it loads, the server is running
2. Check if [plex.tv](https://www.plex.tv) loads (if it doesn't, Plex itself is having issues)
3. Restart your WiFi router
4. Try from your phone using cellular data (not WiFi)

If the page loads but nothing plays, try signing out and back in. If it won't load at all, the server is offline — {{ admin_contact | lower }}.

---

## Smart TV Limitations

!!! warning "Why Your Smart TV Might Struggle"

    Most smart TVs have **weak WiFi** and **slow ethernet ports** (100 Mbps instead of gigabit). This causes buffering, especially with 4K content.

    **Signs your TV is the problem:**

    - Buffering on the TV but not on your phone
    - Works fine at 720p but buffers at 1080p or 4K
    - Ethernet cable doesn't help

If your smart TV struggles with Plex, consider a dedicated streaming device. They have better WiFi, faster processors, and more reliable Plex apps.

### Recommended Streaming Devices

| Device | Price | Best For |
|--------|-------|----------|
| **[Nvidia Shield TV Pro](https://www.nvidia.com/en-us/shield/)** | ~$200 | Best overall - handles everything, lossless audio, 4K AI upscaling |
| **Amazon Fire TV Stick 4K Max** | ~$60 | Great value - reliable 4K, WiFi 6E |
| **[Apple TV 4K](https://www.apple.com/apple-tv-4k/)** | ~$130 | Best for Apple households |
| **[Onn 4K Google TV](https://www.walmart.com/ip/onn-Google-TV-4K-Streaming-Box)** | ~$20 | Budget option - surprisingly capable |

**Recommendation:** If you watch a lot of 4K content or have audio equipment (soundbar/receiver), get the **Nvidia Shield TV Pro**. For most people, the **Fire TV Stick 4K Max** is the sweet spot.

### Device Compatibility Details

Not all devices support every video/audio format. If your device can't play a file directly, the server has to convert it in real-time (transcode), which can reduce quality.

| Device | 4K | HDR/DV | Lossless Audio | HEVC (H.265) |
|--------|:--:|:------:|:--------------:|:------------:|
| **Nvidia Shield TV Pro** | Yes | Yes | Yes | Yes |
| **Apple TV 4K** | Yes | Yes | Partial | Yes |
| **Fire TV Stick 4K Max** | Yes | Yes | No | Yes |
| **Onn 4K Google TV** | Yes | Yes | No | Yes |
| **LG Smart TV** (webOS) | Yes | HDR10/DV | No | Yes |
| **Samsung Smart TV** (Tizen) | Yes | HDR10+ | No | Yes |
| **Sony Smart TV** (Google TV) | Yes | HDR10/DV | No | Yes |
| **TCL Smart TV** (Roku/Google) | Yes | HDR10/DV | No | Yes |
| **Vizio Smart TV** (SmartCast) | Yes | HDR10/DV | No | Varies |
| **Web Browser** | No | No | No | No |

!!! tip "Want the full breakdown?"
    TRaSH Guides maintains a comprehensive [media player compatibility spreadsheet](https://trash-guides.info/Plex/what-does-my-media-player-support/) covering Dolby Vision profiles, HDR formats, audio codecs, and more across dozens of devices.

---

## More Help

<!-- markdownlint-disable MD055 MD056 -->
| Resource | Link |
|----------|------|
| **Plex Support Articles** | [support.plex.tv](https://support.plex.tv/articles/) |
| **Playback Issues** | [Troubleshooting Guide](https://support.plex.tv/articles/200430313-troubleshooting/) |
| **Quality Settings** | [Quality Suggestions](https://support.plex.tv/articles/quality-suggestions/) |
| **Account Help** | [Account Dashboard](https://support.plex.tv/articles/201862428-plex-accounts/) |
| **Plex Plans** | [plex.tv/plans](https://www.plex.tv/plans/) |
{% if has_request_system %}| **Report Content Issue** | [{{ request_url }}](https://{{ request_url }}) |
{% endif %}
<!-- markdownlint-enable MD055 MD056 -->

---

## Account Security

!!! danger "Think someone else is using your account?"
    If your streams keep getting interrupted with a message about unauthorized devices, someone may be sharing your login. Follow these steps to take back control.

### Step 1: Change Your Password

1. Go to [plex.tv/sign-in](https://www.plex.tv/sign-in/) and sign in
2. Click your **profile picture** (top-right) → **Account**
3. Under **Password**, click **Change Password**
4. Pick a strong, unique password you haven't used anywhere else

!!! tip "Password Tips"
    - Use at least 12 characters
    - Don't reuse passwords from other sites
    - Consider using a password manager ([Bitwarden](https://bitwarden.com) is free)

### Step 2: Sign Out of All Devices

After changing your password, force everyone else out:

1. Go to [app.plex.tv](https://app.plex.tv) and sign in
2. Click your **profile picture** (top-right) → **Account** → **Authorized Devices**
3. You'll see every device signed into your account
4. Click the **X** next to any device you don't recognize
5. Sign back in on your own devices

### Step 3: Check Your Email

Make sure no one changed your email address:

1. Go to [plex.tv](https://www.plex.tv) → **Account**
2. Verify the email address is still yours
3. If it was changed, contact [Plex Support](https://support.plex.tv/articles/)

### Not the Account Holder?

If you received a message that you're not authorized to use this account, you need your **own** free Plex account:

1. Go to [plex.tv/sign-up](https://www.plex.tv/sign-up/) and create a free account
2. **{{ admin_contact }} your email address** so they can invite you to {{ server_name }}
3. Check your email for the invitation and click **Accept**

This is free and takes 2 minutes. See [Getting Started](#getting-started-one-time-setup) above for full setup instructions.

<!-- markdownlint-disable MD003 -->
{% if has_migration %}
---

## Switching to a New Account?
<!-- markdownlint-enable MD003 -->

If you need to move to a new Plex account (new email, etc.), {{ admin_name }} can **migrate your entire watch history** to the new account. All your watched/unwatched status transfers over — no need to start from scratch.

1. Create your new account at [plex.tv/sign-up](https://www.plex.tv/sign-up/)
2. {{ admin_contact }} your **new email** and **old username**
3. {{ admin_name }} will transfer your watch history and add you to {{ server_name }}
{% endif %}

---

## Contact {{ admin_name }}

**Only contact {{ admin_name }} for these things:**

- [{{ media_url }}](https://{{ media_url }}){% if has_request_system %} or [{{ request_url }}](https://{{ request_url }}){% endif %} won't load at all (the server or its services are down — not a plex.tv issue)
- You need to be added (send your email address)
{% if has_migration %}- You're switching to a new account ({{ admin_name }} can migrate your watch history)
{% endif %}{% if not has_request_system %}- A movie/show has the wrong audio, bad quality, or missing subtitles
{% endif %}- You're seeing payment prompts when you shouldn't be

{{ contact_card() }}
