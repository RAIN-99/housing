from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HousesAlatauskij, HousesAlmalinskij, HousesAujezovskij, HousesBostandykskij, HousesMedeuskij, HousesNauryzbajskiy, HousesTurksibskij, HousesZhetysuskij, Predictions
from .serializers import HousesAlatauskijSerializer,HousesAlmalinskijSerializer,HousesAujezovskijSerializer,HousesBostandykskijSerializer,HousesMedeuskijSerializer,HousesNauryzbajskiySerializer,HousesTurksibskijSerializer,HousesZhetysuskijSerializer, PredictionSerializer
import pickle
from django.http import JsonResponse, HttpResponse
import pandas as pd
import json
import os

@api_view(["GET"])
def houses_alatauskij(request):
    data = HousesAlatauskij.objects.all()
    serializer = HousesAlatauskijSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def houses_almalinskij(request):
    data = HousesAlmalinskij.objects.all()
    serializer = HousesAlmalinskijSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def houses_aujezovskij(request):
    data = HousesAujezovskij.objects.all()
    serializer = HousesAujezovskijSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def houses_bostandykskij(request):
    data = HousesBostandykskij.objects.all()
    serializer = HousesBostandykskijSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def houses_medeuskij(request):
    data = HousesMedeuskij.objects.all()
    serializer = HousesMedeuskijSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def houses_nauryzbajskiy(request):
    data = HousesNauryzbajskiy.objects.all()
    serializer = HousesNauryzbajskiySerializer(data, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def houses_turksibskij(request):
    data = HousesTurksibskij.objects.all()
    serializer = HousesTurksibskijSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def houses_zhetysuskij(request):
    data = HousesZhetysuskij.objects.all()
    serializer = HousesZhetysuskijSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def analyzeHouse(request):
    print(request)
    data = request.data
    print(data)
    region = request.data['region']
    model = pickle.load(open(f'./models/Xgboost_model_{region}.pkl','rb'))
    x_test = pd.DataFrame([data])
    x_test.drop(columns=["region"],inplace=True)
    prediction = model.predict(x_test)
    prediction_data = Predictions.objects.create(
        number_of_rooms = data['number_of_rooms'],
        floor = data["floor"],
        area = data['area'],
        total_floor = data["total_floor"],
        region = data['region'],
        prediction = prediction[0]
    )
    serializer = PredictionSerializer(prediction_data, many=False)
    print(prediction)
    return Response(serializer.data)
