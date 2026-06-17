import unicodedata

from django.utils.text import slugify as django_slugify

from .settings import get_setting

__all__ = ["slugify"]


def slugify(base):
    normalized = unicodedata.normalize("NFKD", base).encode("ascii", "ignore").decode("ascii")
    return django_slugify(normalized, allow_unicode=get_setting("UNICODE_SLUGS"))