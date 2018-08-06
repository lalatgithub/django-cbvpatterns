Django cbvpatterns
==================

A nicer version of `patterns()` for use with class based views. Inspired
largely by Loic. This is an improved version of [mjtamlyn cbvpatterns](https://github.com/mjtamlyn/django-cbvpatterns) to support latest versions of Django

Django supported versions
-------------
    Django 1.10
    Django 1.11
    Django 2.0
    Django 2.1b1

What is this?
-------------

If you're a big fan of class based views in Django or you want to import views from one module
to another module's `urls.py` you might often find your `urls.py` starting to look a little cluttered. Something like::

    from django.conf.urls import url
    from django.urls import path, re_path # Django >= 2.0

    from account.user import views as userViews
    from github.projects import views as githubViews
    from favorite.wishlist import views as wishlistViews

    # Django < 2.0
    urlpatterns = [
        url(r'^user/login/$', userViews.login, name='login'),
        url(r'^github/projects/$', githubViews.projects, name='projects'),
        url(r'^wishlist/(?P<pk>\d+)/$', wishlistViews.wishlist, name='wishlist-detail'),
    ]

    # Django >= 2.0
    urlpatterns = [
        path('user/login', userViews.login, name='login'),
        path('github/projects', githubViews.projects, name='projects'),
        re_path(r'^wishlist/(?P<pk>\d+)', wishlistViews.wishlist, name='wishlist-detail'),
    ]

So we can now have a class based view or functional view which has the same feel::

    from cbvpatterns import url
    from cbvpatterns import path, re_path # Django >= 2.0

    # no need to import views from other modules

    # Django < 2.0
    urlpatterns = [
        url(r'^user/login/$', 'account.user.views.login', name='login'),
        url(r'^github/projects/$', 'github.projects.views.projects', name='projects'),
        url(r'^wishlist/(?P<pk>\d+)/$', 'favorite.wishlist.views.wishlist', name='wishlist-detail'),
    ]

    # Django >= 2.0
    urlpatterns = [
        path('user/login', 'account.user.views.login', name='login'),
        path('github/projects', 'github.projects.views.projects', name='projects'),
        re_path(r'^wishlist/(?P<pk>\d+)', 'favorite.wishlist.views.wishlist', name='wishlist-detail'),
    ]

You can also pass in the actual view classes directly, rather than using the
string representation.

##### NOTE:
You can only import url from cbvpatterns if you are using Django < 2.0 <br/>
You can only import path, re_path from cbvpatterns if you are using Django >= 2.0

Contributing
------------

Development takes place
`on GitHub <http://github.com/lalzada/django-cbvpatterns>`_; pull requests are
welcome.
