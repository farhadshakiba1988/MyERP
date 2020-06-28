# مشخص کردن نوع فیلدهای برگشتی از مدل JobOffers
from rest_framework import serializers

from candidate.models import Candidate
from jobs.models import JobOffers


class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobOffers
        fields = '__all__'


# مشخص کردن نوع فیلدهای برگشتی از مدل Candidate
class CandidateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
