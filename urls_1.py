from django.urls import path
from polls.views import Home

#cargamos la vista
urlpatterns = [
    path('', Home.as_view(), name='home'), #se renderiza como clase
]



