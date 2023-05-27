
from rest_framework import serializers
from .models import Lender


class LenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lender
        fields = "__all__"