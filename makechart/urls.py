from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'makechart'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('e/', views.EmployeeIndex.as_view(), name='employee-index'),
    path('t<int:pk>/', views.DetailView.as_view(), name='detail'),
#   path('<int:pk>/', views.EmployeeUpdate, name='employee'),
    # modelforms/product/entry
    url(r'^employee/entry/$', views.EmployeeAdd.as_view(), name='employee-entry'),
    # modelforms/product/2
    url(r'^employee/(?P<pk>[0-9]+)/$', views.EmployeeUpdate.as_view(), name='employee-update'),
    # modelforms/product/(?P<pk>[0-9]+)/delete
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.EmployeeDelete.as_view(), name='employee-delete')
]
