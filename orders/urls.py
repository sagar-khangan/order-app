from rest_framework.routers import SimpleRouter
from orders import views


router = SimpleRouter()

router.register(r'orders', views.OrdersViewSet)
router.register(r'orderitems', views.OrderItemsViewSet)

urlpatterns = router.urls
