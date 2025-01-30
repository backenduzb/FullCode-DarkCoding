from django.urls import path
from .views import Home,Posts,AddPost,PythonContent,PostDetailView,GolangContent,JSContent,BatContent,AddContent

urlpatterns=[
    path('',Home.as_view(),name="home"),
    path('python/',PythonContent.as_view(),name="python"),
    path('JS/',JSContent.as_view(),name="JS"),
    path('golang/',GolangContent.as_view(),name="golang"),
    path('bat/',BatContent.as_view(),name="bat"),
    path('bat/<int:pk>/',PostDetailView.as_view(),name="post_detail3"),
    path('python/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('JS/<int:pk>/', PostDetailView.as_view(), name='post_detail1'),
    path('golang/<int:pk>/', PostDetailView.as_view(), name='post_detail2'),
    path('blogs/',Posts.as_view(),name="blogla"),
    path('addposta/', AddPost.as_view(), name='add_post'),  
    path('addcontent/',AddContent.as_view(),name="addcontent")
]
