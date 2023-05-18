from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),

]
# aly b3d al / fe url bta3 project
# alhoa aaaaa hena
# www.site.com/seif/'aaaaa'--> da aly gowah al response bta3 fn al views
# law mesh mwgoda hwslha b /seif/ bas
