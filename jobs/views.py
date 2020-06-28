from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import JobSerializers
from jobs.models import JobOffers


@api_view(['GET'])
def job_list(request):
    """
        1. لیستی از تمام مشاغل را برمیگرداند
    """
    job = JobOffers.objects.all()
    serializer = JobSerializers(job, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def job_detail(request, pk):
    """
        1. لیستی از جزییات شغل رو انتخاب شده رو برمیگرداند
    """
    job = JobOffers.objects.get(id=pk)
    serializer = JobSerializers(job, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def job_create(request):
    """
        1. ایجاد شغل جدید
    """
    serializer = JobSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def job_update(request, pk):
    """
        1. آپدیت زدن روی شغل تیحاد شده
    """
    job = JobOffers.objects.get(id=pk)
    serializer = JobSerializers(instance=job, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def job_delete(request, pk):
    """
    1. پاک کردن شغل انتخاب شده بر اساس آیدی
    """
    task = JobOffers.objects.get(id=pk)
    task.delete()
    return Response('Item successful deleted')
