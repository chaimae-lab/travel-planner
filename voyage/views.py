from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import CritereVoyage
from .serializers_voyage  import CritereVoyageSerializer

from voyage.models import  JourVoyage ,Activite 


#   Récupérer un  critères  via son ID.
@api_view(['GET'])
def recuperer_criteres(request, critere_id):
   
    critere = get_object_or_404(CritereVoyage, id=critere_id)
    serializer = CritereVoyageSerializer(critere)
    return Response(serializer.data)


