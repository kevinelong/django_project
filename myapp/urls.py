from django.conf.urls import patterns, url
from myapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.index, name='about'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^data_categories_count/$', views.data_categories_count, name='data_categories_count'),
    url(r'^data_categories/$', views.data_categories, name='data_categories'),
    url(r'^data_categories_dict/$', views.data_categories_dict, name='data_categories_dict'),
    url(r'^data_pages/$', views.data_pages, name='data_pages'),
    url(r'^data_all/$', views.data_all, name='data_all'),
    url(r'^data_nested/$', views.data_nested, name='data_nested'),
    url(r'^data_both/$', views.data_both, name='data_both'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
)  # New!