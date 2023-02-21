from .models import HousesAlatauskij, HousesAlmalinskij, HousesAujezovskij, HousesBostandykskij, HousesMedeuskij, HousesNauryzbajskiy, HousesTurksibskij, HousesZhetysuskij,Predictions
from rest_framework import serializers



class HousesAlatauskijSerializer(serializers.ModelSerializer):
	class Meta:
		model = HousesAlatauskij
		fields = "__all__"

class HousesAlmalinskijSerializer(serializers.ModelSerializer):
	class Meta:
		model = HousesAlmalinskij
		fields = "__all__"

class HousesAujezovskijSerializer(serializers.ModelSerializer):
	class Meta:
		model = HousesAujezovskij
		fields = "__all__"

class HousesBostandykskijSerializer(serializers.ModelSerializer):
	class Meta:
		model = HousesBostandykskij
		fields = "__all__"
		
class HousesMedeuskijSerializer(serializers.ModelSerializer):
	class Meta:
		model = HousesMedeuskij
		fields = "__all__"

class HousesNauryzbajskiySerializer(serializers.ModelSerializer):
	class Meta:
		model = HousesNauryzbajskiy
		fields = "__all__"

class HousesTurksibskijSerializer(serializers.ModelSerializer):
	class Meta:
		model = HousesTurksibskij
		fields = "__all__"

class HousesZhetysuskijSerializer(serializers.ModelSerializer):
	class Meta:
		model = HousesZhetysuskij
		fields = "__all__"	

class PredictionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Predictions
		fields = "__all__"	
