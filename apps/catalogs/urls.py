from django.conf.urls import url

from .api.v1 import views as api_v1_views
from . import apps

app_name = apps.CatalogConfig.name

urlpatterns = [
    url(
        r'^api/v1/me/$',
        api_v1_views.MeAPIView.as_view(),
        name='me',
    ),
    url(
        r'^api/v1/catalogs/$',
        api_v1_views.CatalogListCreateAPIView.as_view(),
        name='list',
    ),
    url(
        r'^api/v1/catalogs/(?P<pk>\d+)/$',
        api_v1_views.CatalogRetrieveUpdateAPIView.as_view(),
        name='detail',
    ),
    url(
        r'^api/v1/users/(?P<pk>\d+)/$',
        api_v1_views.UserRetrieveUpdateAPIView.as_view(),
        name='detail',
    ),
]
