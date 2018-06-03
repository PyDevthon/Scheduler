from django.urls import path, re_path
from schedule import views

urlpatterns = [
    re_path(r'^$', views.Home.as_view(), name='Home'),
    path('hrworkarea', views.HRWorkArea.as_view(), name='hrworkarea'),
    path('workarea', views.WorkArea.as_view(), name='workarea'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('addcandidate', views.CreateCandidate.as_view(), name='add_candidate')
]

