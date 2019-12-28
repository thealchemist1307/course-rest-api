from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from profiles_api import views
router =DefaultRouter()
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)
router.register('clubs',views.ClubInfoViewSet)

urlpatterns =[
    url(r'^login/',views.UserLoginApiView.as_view()),
    url(r'^',include(router.urls)),

]
