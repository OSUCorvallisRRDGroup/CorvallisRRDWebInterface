from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^sign-in/$', views.sign_in, name='sign_in'),
    url(r'^$', views.sign_in, name='sign_in'),
    url(r'^sign-out/$', views.sign_out, name='sign_out'),

    url(r'^providers/$', views.providers, name='providers'),
    url(r'^providers/new/$', views.new_provider, name='new_provider'),
    url(r'^providers/(?P<provider_id>[0-9]+)/$', views.provider, name='provider'),
    url(r'^providers/edit/(?P<provider_id>[0-9]+)/$', views.edit_provider, name='edit_provider'),
    url(r'^providers/delete/(?P<provider_id>[0-9]+)/$', views.delete_provider, name='delete_provider'),

    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/new/$', views.new_category, name='new_category'),
    url(r'^categories/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'^categories/edit/(?P<category_id>[0-9]+)/$', views.edit_category, name='edit_category'),
    url(r'^categories/delete/(?P<category_id>[0-9]+)/$', views.delete_category, name='delete_category'),

    url(r'^items/$', views.items, name='items'),
    url(r'^items/new/$', views.new_item, name='new_item'),
    url(r'^items/(?P<item_id>[0-9]+)/$', views.item, name='item'),
    url(r'^items/edit/(?P<item_id>[0-9]+)/$', views.edit_item, name='edit_item'),
    url(r'^items/delete/(?P<item_id>[0-9]+)/$', views.delete_item, name='delete_item'),

    url(r'^links/$', views.links, name='links'),
    url(r'^links/(?P<link_id>[0-9]+)/$', views.link, name='link'),
    url(r'^links/edit/(?P<link_id>[0-9]+)/$', views.edit_link, name='edit_link'),
]