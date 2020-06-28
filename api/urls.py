from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import JobOffersListView, JobOffersCreateAPIView, \
    JobOffersUpdateAPIView, JobOffersDeleteAPIView, JobOffersDetailAPIView, CandidateViewSet

urlpatterns = [
    path('job_list/', JobOffersListView.as_view(), name='job_list'),
    path('job_create/', JobOffersCreateAPIView.as_view(), name='job_create'),
    path('<pk>', JobOffersDetailAPIView.as_view(), name='job_detail'),
    path('<pk>/job_delete/', JobOffersDeleteAPIView.as_view(), name='job_delete'),
    path('<pk>/job_update/', JobOffersUpdateAPIView.as_view(), name='job_update')

]


router = DefaultRouter()
router.register(r'', CandidateViewSet, basename='candidate')
urlpatterns = router.urls
