from django.urls import path
from . import views
urlpatterns = [
    path('blog-apiview',views.BlogAPIView.as_view())
]
