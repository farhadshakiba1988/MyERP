from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from api.serializers import JobSerializers, CandidateSerializers
from candidate.models import Candidate
from jobs.models import JobOffers


class JobOffersListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = JobSerializers
    queryset = JobOffers.objects.all()


class JobOffersDetailAPIView(RetrieveAPIView):
    queryset = JobOffers.objects.all()
    serializer_class = JobSerializers


class JobOffersCreateAPIView(CreateAPIView):
    queryset = JobOffers.objects.all()
    serializer_class = JobSerializers


class JobOffersDeleteAPIView(DestroyAPIView):
    queryset = JobOffers.objects.all()
    serializer_class = JobSerializers


class JobOffersUpdateAPIView(UpdateAPIView):
    queryset = JobOffers.objects.all()
    serializer_class = JobSerializers


class CandidateViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CandidateSerializers
    queryset = Candidate.objects.all()
