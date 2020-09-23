from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),  #a map to index.html, empty path means just '/polls'
    path('<int:question_id>/', views.detail, name='detail'),            # question_id is a parameter (same name) from detail method
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')   # for voting to be enabled

]