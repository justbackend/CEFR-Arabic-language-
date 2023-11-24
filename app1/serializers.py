from rest_framework import serializers
from .models import *

class Part1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part1
        fields = "__all__"

class Part2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part2
        fields = "__all__"

class Part3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part3
        fields = "__all__"

class TimeSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_Settings
        fields = "__all__"


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoNotEnter
        fields = "__all__"


class TestTakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTaker
        fields = "__all__"


class JuzAudioSerializer(serializers.Serializer):
    class Meta:
        model = JuzAudio
        fields = "__all__"
