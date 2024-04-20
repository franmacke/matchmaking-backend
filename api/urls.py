from rest_framework import routers
from api.viewsets.PlayerViewset import PlayerViewset
from api.viewsets.MatchViewset import MatchViewset
from api.viewsets.PlayerMatchDetailsViewset import PlayerMatchDetailsViewset
from api.viewsets.PositionsViewset import PositionsViewset

router = routers.DefaultRouter()

router.register(r'player', PlayerViewset)
router.register(r'match', MatchViewset)
router.register(r'playermatchdetails', PlayerMatchDetailsViewset)   
router.register(r'positions', PositionsViewset)

urlpatterns = router.urls
