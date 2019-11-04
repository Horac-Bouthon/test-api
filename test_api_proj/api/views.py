import ast
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.

class PatexViewset(viewsets.ModelViewSet):
    """ API view set to test patex crawler """
    serializer_class = serializers.PatexSeralizer
    queryset = models.PatexData.objects.all()

class BatchView(APIView):
    def get(self, request, format=None):
        an_apiview = list()
        for obj in models.PatexData.objects.all():
            new_dict = dict()
            new_dict["ID"] = obj.pk
            new_dict["classification"] = obj.classification
            new_dict["product_name"] = obj.product_name
            new_dict["bar_code"] = obj.bar_code
            an_apiview.append(new_dict)
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = serializers.BatchSerializer(data=request.data)
        my_counter = 0
        for line in request.data.get("products"):
            print(line['product_name'], line['bar_code'])
            bar_code = line['bar_code']
            test = models.PatexData.objects.filter(bar_code=bar_code)
            if not test:
                str_feat = ""
                for f_l in line['features']:
                    str_feat += f_l
                    str_feat += '\n'
                str_rech = ""
                for t_l in line['tech_url']:
                    str_rech += t_l
                    str_rech += '\n'
                str_sec = ""
                for s_l in line['security_url']:
                    str_sec += s_l
                    str_sec += '\n'
                data_line = models.PatexData(
                    classification=line['category'],
                    product_name=line['product_name'],
                    image_url=line['image_url'],
                    description=line['description'],
                    features=str_feat,
                    tech_url=str_rech,
                    security_url=str_sec,
                    bar_code=bar_code,
                )
                data_line.save()
                my_counter += 1
        message = 'Created {0} lines.'.format(my_counter)
        return Response({'message': message})


"""
    classification
    product_name
    image_url
    description
    features
    tech_url
    security_url
    bar_code
"""
