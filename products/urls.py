from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .models import ProductViewHistory
from .services.flash_sale import FlashSaleListCreateView
from .views import ProductViewSet, ReviewViewSet, CategoryViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('reviews', ReviewViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('sale/', FlashSaleListCreateView.as_view(), name='sale'),
    path('check-sale/<int:product_id>/', check_flash_sale, name='product-view-history-create'),
    path('product-view/', ProductViewHistoryCreate.as_view(), name='product-view-history-create'),
]