from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.index,name="index"),
    path("home",views.index,name="home"),
    path("about_artist",views.about_artist,name="about_artist"),
    path("portfolio1",views.portfolio1,name="portfolio1"),
    path("portfolio2",views.portfolio2,name="portfolio2"),
    path("portfolio3",views.portfolio3,name="portfolio3"),
    path("contact",views.contact,name="contact"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("search",views.search,name="search"),
    path("logout",views.logout,name="logout"),
    path("login_user",views.login_user,name="login_user"),
    path("login_home",views.login_user,name="login_home"),
    path("googleLogin",views.googleLogin,name="googleLogin")
]
urlpatterns=urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)