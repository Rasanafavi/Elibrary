# Create web/urls.py and paste the following
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.Purple.as_view(), name="purple"),
    path("form/", views.Forms.as_view(), name="forms"),
    path("icon/", views.Icons.as_view(), name="icons"),
    path("buttons/", views.Buttons.as_view(), name="buttons"),
    path("typography/", views.Typography.as_view(), name="typography"),
    path("charts/", views.Charts.as_view(), name="charts"),
    path("tables/", views.Tables.as_view(), name="tables"),
    path("error/", views.Error.as_view(), name="error"),

    path("book-create/", views.BookCreate.as_view(), name="bookcreate"),
    path("book-list/", views.BookList.as_view(), name="booklist"),
    path("book-detail/<str:pk>/", views.BookDetail.as_view(), name="bookdetail"),
    path("book-update/<str:pk>/", views.BookUpdate.as_view(), name="bookupdate"),
    path("book-delete/<str:pk>/", views.BookDelete.as_view(), name="bookdelete"),


    path("author-create/", views.authorCreate.as_view(), name="authorcreate"),
    path("author-list/", views.authorList.as_view(), name="authorlist"),
    path("author-detail/<str:pk>/", views.authorDetail.as_view(), name="authordetail"),
    path("author-update/<str:pk>/", views.authorUpdate.as_view(), name="authorupdate"),
    path("author-delete/<str:pk>/", views.authorDelete.as_view(), name="authordelete"),



]

# from . import views
# from django.urls import path

# app_name='app'

# urlpatterns=[
#     path("",views.purple,name="purple"),
#     path("charts/",views.charts,name="charts"),
#     path("forms/",views.forms,name="forms"),
#     path("mdi/",views.icons,name="icons"),
#     path("login/",views.login,name="login"),
#     path("register/",views.register,name="register"),
#     path("tables/",views.tables,name="tables"),
#     path("buttons/",views.buttons,name="buttons"),
#     path("typography/",views.typography,name="typography"),

# ]