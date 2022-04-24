from django.urls import path, include

from rest_framework.routers import DefaultRouter

from API import views



router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('interview-slots', views.InterviewSlotViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('active-slots/', views.ActiveSlotList.as_view()),
]