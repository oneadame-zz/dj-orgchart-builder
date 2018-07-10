from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'makechart'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('e/', views.EmployeeIndex.as_view(), name='employee-index'),
    path('t<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:team_id>/confirm_update/', views.confirm_update, name='confirm-update'),
    path('<int:employee_id>/confirm_employee_update/', views.confirm_emp_update, name='confirm-emp-update'),
    #orchartmaker/employee/entry
    url(r'^employee/entry/$', views.EmployeeAdd.as_view(), name='employee-entry'),
    #orchartmaker/employee/2
    url(r'^employee/(?P<pk>[0-9]+)/$', views.EmployeeUpdate.as_view(), name='employee-update'),
    #orchartmaker/employee/(?P<pk>[0-9]+)/delete
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.EmployeeDelete.as_view(), name='employee-delete'),
    #orchartmaker/team/entry
    url(r'^team/entry/$', views.TeamAdd.as_view(), name='team-entry'),
    #orchartmaker/team/2
    url(r'^team/(?P<pk>[0-9]+)/$', views.TeamUpdate.as_view(), name='team-update'),
    #orchartmaker/team/(?P<pk>[0-9]+)/delete
    url(r'^t/(?P<pk>[0-9]+)/delete$', views.TeamDelete.as_view(), name='team-delete'),
    url(r'^teammembers/(?P<pk>[0-9]+)/$', views.TeamMemberUpdate.as_view(), name='team-member-update'),
    url(r'^teammembersadd/(?P<pk>[0-9]+)/$', views.add_member, name='team-member-add'),
    url(r'^teammembersrm/(?P<pk>[0-9]+)/$', views.rm_member, name='team-member-rm')
]
