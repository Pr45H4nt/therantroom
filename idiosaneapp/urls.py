from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.homeview , name = 'home' ),
    path('article/<slug>', views.ArticleView, name= 'article'),
    path('write_article', views.create_article, name= "write_article"),
    path('about', views.about, name= "about"),
    path('donate', views.donate, name= "donate"),
    path('feedback', views.feedback, name= "feedback"),
    path('blowmymind', views.blowmymind, name= "blowmymind"),
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)