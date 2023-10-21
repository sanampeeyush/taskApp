from django.urls import path
from .views import (
    BusinessCreateView, 
    BusinessUpdateView, 
    BusinessDeleteView, 
    BusinessListView,
    BusinessByIDView,
    BusinessByNameView,
)

urlpatterns = [
    path('business/', BusinessCreateView.as_view(), name='business_create'),
    path('business/<int:pk>/', BusinessUpdateView.as_view(), name='business_update'),
    path('business/<int:pk>/delete/', BusinessDeleteView.as_view(), name='business_delete'),
    path('business/list/', BusinessListView.as_view(), name='business_list'),
    path('business/id/<int:id>/', BusinessByIDView.as_view(), name='business_by_id'),
    path('business/name/<str:name>/', BusinessByNameView.as_view(), name='business_by_name'),
]
