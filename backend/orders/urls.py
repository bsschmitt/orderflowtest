#Criando o router automatico.
from rest_framework.routers import DefaultRouter
from .views import ORderViewSet

router = DefaultRouter()

router.register(
    r'orders',
    ORderViewSet,
    basename = 'order'
)

urlpatterns = router.urls