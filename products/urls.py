from rest_framework import routers
from .views import ProductMVS,CategoryMVS,ProductAllMVS


router = routers.DefaultRouter()
router.register('products', ProductMVS)
router.register('category', CategoryMVS)
router.register('productsall', ProductAllMVS)

urlpatterns = router.urls