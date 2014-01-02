from django import template
from django.utils.html import format_html
from django.contrib.admin.templatetags.admin_static import static


register = template.Library()


@register.filter
def boolean_icon(value):
    icon_url = static('admin/img/icon-%s.gif' %
                      {True: 'yes', False: 'no', None: 'unknown'}[value])
    alt_text = {True: 'yes', False: 'no', None: 'pending' }[value]
    return format_html('<img src="{0}" alt="{1}" />', icon_url, alt_text)
