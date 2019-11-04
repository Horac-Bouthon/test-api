from rest_framework import serializers

from . import models

class PatexSeralizer(serializers.ModelSerializer):
    """ Serializer for model objects """
    class Meta:
        model = models.PatexData
        fields = ('id', 'classification', 'product_name', 'image_url',
            'description', 'features', 'tech_url', 'security_url',
            'bar_code',)

    def create(self, validated_data):
        """ Create and rerurn a new line """
        line = models.PatexData(
            classification = validated_data["classification"],
            product_name = validated_data["product_name"],
            image_url = validated_data["image_url"],
            description = validated_data["description"],
            features = validated_data["features"],
            tech_url = validated_data["tech_url"],
            security_url = validated_data["security_url"],
            bar_code = validated_data["bar_code"],
        )
        line.save()
        return line


class BatchSerializer(serializers.Serializer):
    products = serializers.ListField(
        child=serializers.CharField(max_length=1500),
        allow_empty=True,
        )
