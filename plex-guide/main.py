"""MkDocs Macros hook — contact card with bot-protection and metadata resolution.

Provides:
  - contact_card(): Bot-protected contact info (base64-encoded, JS-decoded)
  - Frontmatter variable resolution ({{ server_name }} in title/description)
"""

import base64
import re

from markupsafe import Markup


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
            badge = (
                ' <span class="preferred-badge">preferred</span>' if preferred else ""
            )

            href = _build_href(method_type, value)
            display_value = _display_value(method_type, value)

            # noscript fallback with plain value
            noscript_link = (
                f'<a href="{href}" rel="nofollow noopener noreferrer">{display_value}</a>'
                if href != value
                else f"<span>{display_value}</span>"
            )

            items_html.append(
                f'<li id="{elem_id}">'
                f"<strong>{label}</strong>{badge}: "
                f"<noscript>{noscript_link}</noscript>"
                f"</li>"
            )

            js_decoders.append(
                f'  decode("{elem_id}", "{encoded}", "{label}", "{method_type}", {str(preferred).lower()});'
            )

        if not items_html:
            return Markup("")

        items = "\n".join(items_html)
        decoders = "\n".join(js_decoders)

        html = f"""\
<div class="contact-card">
<ul>
{items}
</ul>
</div>
<script>
(function() {{
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
      }} else {{
        href = decoded;
        display = label;
      }}
      elem.innerHTML = '<strong>' + label + '</strong>' + badge + ': '
        + '<a href="' + href + '" rel="nofollow noopener noreferrer">' + display + '</a>';
    }} catch (e) {{
      // Decoding failed — noscript fallback remains
    }}
  }}
{decoders}
}})();
</script>"""

        return Markup(html)


def _build_href(method_type, value):
    """Build the appropriate href for a contact method type."""
    if method_type == "email":
        return f"mailto:{value}"
    if method_type == "phone":
        digits = re.sub(r"[^\d+]", "", value)
        return f"tel:{digits}"
    return value


def _display_value(method_type, value):
    """Build a display string for noscript fallback."""
    if method_type in ("email", "phone"):
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
