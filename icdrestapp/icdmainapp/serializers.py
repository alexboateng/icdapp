from rest_framework import serializers
from .models import ICDVersion
from .models import ICDCode

class ICDVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICDVersion
        fields = "__all__"

class ICDCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICDCode
        fields = "__all__"