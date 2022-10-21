from rest_framework import serializers
from .models import *
from rest_framework_gis.serializers import GeoModelSerializer


class RewardsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rewards
        fields = '__all__'


class TreeShopSerializer(GeoModelSerializer):
    class Meta:
        model = TreeShop
        fields = '__all__'


class TreeSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='get_category_display')
    class Meta:
        model = Tree
        fields = '__all__'


class TreeOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TreeOrder
        fields = '__all__'


class TreeShopSerializerDetail(GeoModelSerializer):
    trees = serializers.SerializerMethodField('get_trees')

    class Meta:
        model = TreeShop
        fields = '__all__'

    def get_trees(self, obj):
        trees = Tree.objects.filter(shop=obj)
        return TreeSerializer(trees, many=True).data


class RecycleAreaSeriailizer(GeoModelSerializer):

    class Meta:
        model = RecycleArea
        fields = '__all__'

class RecycleCallSerializer(GeoModelSerializer):
    class Meta:
        model = RecycleCall
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}


class CampaignSerializer(GeoModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'


class CampaignInvolvementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignInvolvement
        fields = '__all__'
        extra_kwargs = {'user': {'required': False},
                        'campaign': {'required': False}}


class CampaignSerializerDetail(GeoModelSerializer):
    involvements = serializers.SerializerMethodField('get_involvements')

    class Meta:
        model = Campaign
        fields = '__all__'

    def get_involvements(self, obj):
        qs = CampaignInvolvement.objects.filter(campaign=obj)
        return CampaignInvolvementSerializer(qs, many=True).data
