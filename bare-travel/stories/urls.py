from django.conf.urls import url

from .views import StoryCreateView, StoryDeleteView, StoryDetailView, StoryListView, StoryUpdateView

urlpatterns = [
    url(r'^$', StoryListView.as_view(), name='list'),
    url(r'^create/$', StoryCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', StoryDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', StoryUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', StoryDeleteView.as_view(), name='delete'),
]