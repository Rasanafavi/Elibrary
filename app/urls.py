from . import views
from django.urls import path

app_name='app'

urlpatterns=[
    path("",views.purple,name="purple"),
    path("chart",views.chart,name="chart"),
    path("forms",views.forms,name="forms"),
    path("icons",views.icons,name="icons"),
    path("tables",views.tables,name="tables"),
    path("buttons",views.buttons,name="buttons"),
    path("typography",views.typography,name="typography"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
]