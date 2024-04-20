from rest_framework import viewsets
from api.models import Match, MatchDetails
from api.serializers import MatchSerializer, MatchDetailsSerializer
from rest_framework.response import Response
from rest_framework import status

class MatchViewset(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        details = MatchDetails.objects.filter(match_id=instance.id)

        details_serializer = MatchDetailsSerializer(details, many=True)

        return Response({"match": data, "details": details_serializer.data}, status=status.HTTP_200_OK)