from unicodedata import category
from django.urls import path
# from . import views
from .views import HomeView, ArticalView, AddBlog, UpdateBlog, DeleteBlog, Addcategory, categoryView, LikeView, AddCommentView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('blogpost/<int:pk>', ArticalView.as_view(), name='blogpost'),
    path('add_post/', AddBlog.as_view(), name='add_page'),
    path('blogpost/edit/<int:pk>/', UpdateBlog.as_view(), name='edit'),
    path('blogpost/delete/<int:pk>/', DeleteBlog.as_view(), name='delete'),
    path('add_category/', Addcategory.as_view(),name='category'),
    path('category/<str:cats>/', categoryView, name="category_page"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('blogpost/<int:pk>/comments', AddCommentView.as_view(), name='add_comment')
]
