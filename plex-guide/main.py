"""MkDocs Macros hook — contact card with bot-protection and metadata resolution.

Provides:
  - contact_card(): Bot-protected contact info (base64-encoded, JS-decoded)
  - Frontmatter variable resolution ({{ server_name }} in title/description)
"""

import base64
import html as html_mod
import json
import re

from markupsafe import Markup

# Contact types that display as plain text (no clickable link)
_NO_LINK_TYPES = frozenset({"signal_username", "discord"})

# Allowed URL scheme prefixes for href attributes
_ALLOWED_SCHEMES = ("mailto:", "tel:", "sms:", "https://", "http://")


def define_env(env):
    """Register macros environment."""

    @env.macro
    def contact_card(admin_name=None, contact_methods=None):
        """Render bot-protected contact card from config.

        Reads admin_name and contact_methods from extra: config if not passed.
        Base64-encodes values at build time; JavaScript decodes at runtime.

        Args:
            admin_name: Display name for the admin. Falls back to extra.admin_name.
            contact_methods: List of contact method dicts. Falls back to extra.contact_methods.

        Returns:
            Markup with encoded contact info and JS decoder.
        """
        extra = env.conf.get("extra", {})
        admin_name = admin_name or extra.get("admin_name", "Admin")
        contact_methods = contact_methods or extra.get("contact_methods", [])

        if not contact_methods:
            return Markup("")

        items_html = []
        js_decoders = []

        for i, method in enumerate(contact_methods):
            method_type = method.get("type", "link")
            label = method.get("label", "Contact")
            value = method.get("value", "")
            preferred = method.get("preferred", False)

            if not value:
                continue

            encoded = base64.b64encode(value.encode()).decode("ascii")
            elem_id = f"contact-{i}"
            safe_label = html_mod.escape(label)
            badge = (
                ' <span class="preferred-badge">preferred</span>' if preferred else ""
            )

            href = _build_href(method_type, value)
            display_value = _display_value(method_type, value)

            # noscript fallback — use type-based check, not href equality
            if method_type in _NO_LINK_TYPES:
                noscript_content = f"<span>{html_mod.escape(display_value)}</span>"
            elif href:
                noscript_content = (
                    f'<a href="{html_mod.escape(href, quote=True)}"'
                    f' rel="nofollow noopener noreferrer">'
                    f"{html_mod.escape(display_value)}</a>"
                )
            else:
                noscript_content = f"<span>{html_mod.escape(display_value)}</span>"

            items_html.append(
                f'<li id="{elem_id}">'
                f"<strong>{safe_label}</strong>{badge}: "
                f"<noscript>{noscript_content}</noscript>"
                f"</li>"
            )

            # Use json.dumps for safe JS string interpolation
            js_decoders.append(
                f"  decode({json.dumps(elem_id)}, {json.dumps(encoded)},"
                f" {json.dumps(label)}, {json.dumps(method_type)},"
                f" {str(preferred).lower()});"
            )

        if not items_html:
            return Markup("")

        items = "\n".join(items_html)
        decoders = "\n".join(js_decoders)

        html_out = f"""\
<style>
.contact-card {{
  border: 1px solid var(--md-default-fg-color--lighter, #e0e0e0);
  border-radius: 8px;
  padding: 1rem 1.5rem;
  margin: 1rem 0;
  background: var(--md-code-bg-color, #f5f5f5);
}}
.contact-card ul {{
  list-style: none;
  margin: 0;
  padding: 0;
}}
.contact-card li {{
  padding: 0.4rem 0;
}}
.contact-card li + li {{
  border-top: 1px solid var(--md-default-fg-color--lightest, #eee);
}}
.preferred-badge {{
  font-size: 0.75em;
  background: var(--md-accent-fg-color, #448aff);
  color: white;
  padding: 0.15em 0.5em;
  border-radius: 4px;
  vertical-align: middle;
}}
</style>
<div class="contact-card">
<ul>
{items}
</ul>
</div>
<script>
(function() {{
  function esc(s) {{
    var d = document.createElement('div');
    d.appendChild(document.createTextNode(s));
    return d.innerHTML;
  }}
  function decode(id, encoded, label, type, preferred) {{
    var elem = document.getElementById(id);
    if (!elem) return;
    try {{
      var decoded = atob(encoded);
      var badge = preferred ? ' <span class="preferred-badge">preferred</span>' : '';
      var href, display;
      if (type === 'email') {{
        href = 'mailto:' + decoded;
        display = decoded;
      }} else if (type === 'phone') {{
        href = 'tel:' + decoded.replace(/[^+\\d]/g, '');
        display = decoded;
      }} else if (type === 'signal_url') {{
        href = decoded;
        display = label;
      }} else if (type === 'signal_username' || type === 'discord') {{
        elem.innerHTML = '<strong>' + esc(label) + '</strong>' + badge + ': ' + esc(decoded);
        return;
      }} else if (type === 'telegram') {{
        href = 'https://t.me/' + encodeURIComponent(decoded);
        display = decoded;
      }} else if (type === 'whatsapp') {{
        href = 'https://wa.me/' + decoded.replace(/[^+\\d]/g, '');
        display = decoded;
      }} else if (type === 'imessage') {{
        href = 'sms:' + decoded.replace(/[^+\\d]/g, '');
        display = decoded;
      }} else {{
        href = decoded;
        display = label;
      }}
      if (!/^(mailto:|tel:|sms:|https?:\/\/)/.test(href)) {{
        elem.innerHTML = '<strong>' + esc(label) + '</strong>' + badge + ': ' + esc(display);
        return;
      }}
      elem.innerHTML = '<strong>' + esc(label) + '</strong>' + badge + ': '
        + '<a href="' + esc(href) + '" rel="nofollow noopener noreferrer">' + esc(display) + '</a>';
    }} catch (e) {{
      // Decoding failed — noscript fallback remains
    }}
  }}
{decoders}
}})();
</script>"""

        return Markup(html_out)


def _build_href(method_type, value):
    """Build the appropriate href for a contact method type."""
    if method_type == "email":
        return f"mailto:{value}"
    if method_type in ("phone", "imessage"):
        digits = re.sub(r"[^\d+]", "", value)
        prefix = "sms:" if method_type == "imessage" else "tel:"
        return f"{prefix}{digits}"
    if method_type == "telegram":
        return f"https://t.me/{value}"
    if method_type == "whatsapp":
        digits = re.sub(r"[^\d+]", "", value)
        return f"https://wa.me/{digits}"
    if method_type == "signal_url":
        if not any(value.startswith(s) for s in ("https://", "http://")):
            return ""
        return value
    if method_type in _NO_LINK_TYPES:
        return ""
    # Generic link — validate scheme
    if not any(value.startswith(s) for s in ("https://", "http://")):
        return ""
    return value


def _display_value(method_type, value):
    """Build a display string for noscript fallback."""
    if method_type in (
        "email",
        "phone",
        "signal_username",
        "discord",
        "telegram",
        "whatsapp",
        "imessage",
    ):
        return value
    if method_type == "signal_url":
        return "Signal"
    return "Link"


def on_pre_page_macros(env):
    """Resolve Jinja2 expressions in page metadata before rendering."""
    extra = env.conf.get("extra", {})
    page = env.page

    for key in ("title", "description"):
        value = page.meta.get(key, "")
        if "{{" in str(value):
            resolved = re.sub(
                r"\{\{\s*(\w+)\s*\}\}",
                lambda m: str(extra.get(m.group(1), m.group(0))),
                str(value),
            )
            page.meta[key] = resolved
            if key == "title":
                page.title = resolved
