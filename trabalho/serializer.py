from rest_framework import serializers
from trabalho.models import Vitin

class vitinSerializers(serializers.ModelSerializer):

    class Meta:
        model = Vitin
        fields = "__all__"