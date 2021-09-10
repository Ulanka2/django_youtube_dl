from django.urls import path
from .views import  *
urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('dow/', DownloadView.as_view(), name='download')

]

