from rest_framework import routers
from api.viewsets.PlayerViewset import PlayerViewset
from api.viewsets.MatchViewset import MatchViewset
from api.viewsets.MatchDetailsViewset import MatchDetailsViewset

router = routers.DefaultRouter()

router.register(r'player', PlayerViewset)
router.register(r'match', MatchViewset)
router.register(r'matchdetails', MatchDetailsViewset)   

urlpatterns = router.urls
