from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('treeshop', TreeShopViewSet, basename='treeshops')
router.register('recycle', RecycleAreaViewSet, basename='recycleareas')
router.register('campaign', CampaignViewSet, basename='campaigns')
router.register('report', ReportViewSet, basename='reports')
router.register('tree/order', TreeOrderViewSet, basename='treeorder')
urlpatterns = [
    path('near/treeshop/', location_treeshops),
    path('near/recycle/', location_recycle),
    path('near/campaign/', location_campaign),
    path('campaign/involve/<int:id>/', involve_campaign),

]+router.urls
