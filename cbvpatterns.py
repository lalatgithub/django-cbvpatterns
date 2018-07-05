from django.core.exceptions import ImproperlyConfigured
from django.utils import six
from django.views.generic import View
from django.core.urlresolvers import RegexURLPattern, RegexURLResolver, get_callable


class CBVRegexURLPattern(RegexURLPattern):
    _callback_processed = None

    def __init__(self, regex, callback, default_args=None, name=None):
        super(CBVRegexURLPattern, self).__init__(regex, callback, default_args, name)
        if isinstance(self.callback, type) and issubclass(self.callback, View):
            self.callback = callback.as_view()


def url(regex, view, kwargs=None, name=None, prefix=''):
    """As url() in Django."""
    if isinstance(view, (list, tuple)):
        # For include(...) processing.
        urlconf_module, app_name, namespace = view
        return RegexURLResolver(regex, urlconf_module, kwargs, app_name=app_name, namespace=namespace)
    else:
        if isinstance(view, six.string_types):
            if not view:
                raise ImproperlyConfigured('Empty URL pattern view name not permitted (for pattern %r)' % regex)
            if prefix:
                view = prefix + '.' + view

            view = get_callable(view)
        return CBVRegexURLPattern(regex, view, kwargs, name)
