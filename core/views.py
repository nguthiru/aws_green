from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from core.models import Campaign, CampaignInvolvement, RecycleArea, Report, TreeShop
from django.contrib.gis.measure import D
from core.serializers import CampaignInvolvementSerializer, CampaignSerializer, CampaignSerializerDetail, RecycleAreaSeriailizer, ReportSerializer, TreeShopSerializer, TreeShopSerializerDetail
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import GEOSGeometry
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


def get_point(request) -> Point:
    if 'lat' in request.query_params and 'long' in request.query_params:
        lat = request.query_params.get('lat')
        lon = request.query_params.get('long')
        latitude = float(lat)
        longitude = float(lon)
        return Point((longitude, latitude))
    else:
        return None


location_error_text = "Parameters lat and lon are missing"


@api_view(['GET'])
def location_treeshops(request):
    point = get_point(request)
    if point != None:
        qs = TreeShop.objects.filter(location__distance_lte=(point, D(km=2)))
        serial = TreeShopSerializer(qs, many=True)
        return Response(serial.data)
    else:
        return Response(location_error_text, status=400)


@api_view(['GET'])
def location_recycle(request):
    point = get_point(request)
    if point != None:
        qs = RecycleArea.objects.filter(
            location__distance_lte=(point, D(km=2)))
        serial = RecycleAreaSeriailizer(qs, many=True)
        return Response(serial.data)
    else:
        return Response(location_error_text, status=400)


@api_view(['GET'])
def location_campaign(request):
    point = get_point(request)
    if point != None:
        qs = Campaign.objects.filter(location__distance_lte=(point, D(km=2)))
        serial = CampaignSerializer(qs, many=True)
        return Response(serial.data)
    else:
        return Response(location_error_text, status=400)


class TreeShopViewSet(ModelViewSet):

    serializer_class = TreeShopSerializer

    def get_queryset(self):
        return TreeShop.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TreeShopSerializerDetail
        else:
            super().get_serializer_class()


class RecycleAreaViewSet(ModelViewSet):

    serializer_class = RecycleAreaSeriailizer

    def get_queryset(self):
        return RecycleArea.objects.all()


class CampaignViewSet(ModelViewSet):
    serializer_class = CampaignSerializer

    def get_queryset(self):
        return Campaign.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CampaignSerializerDetail
        else:
            super().get_serializer_class()


@api_view(['GET'])
def involve_campaign(request, id):
    campaign = get_object_or_404(Campaign, id=id)

    involvement = CampaignInvolvement(user=request.user, campaign=campaign)

    serializer = CampaignInvolvementSerializer(involvement,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=201)
    else:
        return Response(serializer.errors, status=400)


class ReportViewSet(ModelViewSet):

    serializer_class = ReportSerializer

    def get_queryset(self):
        return Report.objects.all()

    def create(self, request, *args, **kwargs):

        report = Report(user=request.user)

        serial = ReportSerializer(report, **request.data)
        if serial.is_valid():
            serial.save()
            return Response('Your report has been received', 200)
        else:
            return Response(serial.errors, status=400)
