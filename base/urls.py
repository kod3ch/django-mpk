from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', views.admin_dashboard, name="admin_dashboard"),
    path('sales_statistics/', views.sales_statistics, name="sales_statistics"),
    path('registration/', views.register_user, name="registration"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('price_list/', views.price_list, name="price_list"),
    path('store/', views.store, name="store"),
    path('terms/', views.terms, name="terms"),
    path('gdpr/', views.gdpr, name="gdpr"),
    path('about_us/', views.about_us, name="about_us"),
    path('careers/', views.careers, name="careers"),
    path('media/', views.media, name="media"),
    path('contact/', views.contact, name="contact"),
]
