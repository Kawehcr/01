from django.urls import path
from trabalho.views import VitincreateViewSet
from trabalho.views import VitinRetrieveUpdateDeleteViewSet
from trabalho.views import VitinListViewSet
from trabalho.views import RequestTestAPI
from .docs import schema_view

urlpatterns = [
    path('api/v1/Vitins/create', VitincreateViewSet.as_view(), name = 'Vitin_create'),

    path('api/v1/Vitins/<int:pk>/retrieve', VitinRetrieveUpdateDeleteViewSet.as_view(),name = 'Vitin_retrieve'),

    path('api/v1/Vitins/<int:pk>/update', VitinRetrieveUpdateDeleteViewSet.as_view(), name = 'Vitin_update'),

    path('api/v1/Vitins/<int:pk>/destroy', VitinRetrieveUpdateDeleteViewSet.as_view(), name = 'Vitin_destroy'),

    path('api/v1/Vitins/list', VitinListViewSet.as_view(), name = 'Vitin_list'),

    path('api/v1/request/',RequestTestAPI.as_view(), name = 'Vitin_test'),

    path('docs/', schema_view.with_ui ('swagger', cache_timeout = None), name = 'schema-swagger-ui'),

    path('redoc/', schema_view.with_ui ('redoc', cache_timeout = None), name = 'schema-redoc')
]