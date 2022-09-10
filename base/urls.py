import imp
from django.urls import path
from .views import TaskList,TaskDeatail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,CustomFormView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name = 'login'),
    path('logout/',LogoutView.as_view(next_page = 'login'),name = 'logout'),
    path('register/',CustomFormView.as_view(),name="register"),
    path('',TaskList.as_view(),name = 'tasks'),
    path('task/<int:pk>/',TaskDeatail.as_view(),name = 'task'),
    path('taskcreate/',TaskCreate.as_view(),name = 'taskcreate'),
    path('taskupdate/<int:pk>/',TaskUpdate.as_view(),name='taskupdate'),
    path('taskdelete/<int:pk>/',TaskDelete.as_view(),name='taskdelete')

]
