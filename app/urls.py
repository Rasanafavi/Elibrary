

from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.Index.as_view(), name="purple"),
    path("form/", views.Form.as_view(), name="forms"),
    path("icon/", views.Icon.as_view(), name="icons"),
    path("buttons/", views.Button.as_view(), name="buttons"),
    path("typography/", views.Typography.as_view(), name="typography"),
    path("charts/", views.Chart.as_view(), name="chart"),
    path("tables/", views.Table.as_view(), name="tables"),

    path("booklist/", views.BookList.as_view(), name="booklist"),
    path("createbook/", views.BookCreate.as_view(), name="createbook"),
    path("Bookdelete/<str:pk>/", views.BookDelete.as_view(), name="bookdelete"),
    path("update/<str:pk>/", views.BookUpdate.as_view(), name="bookupdate"),
    path("detail/<str:pk>/", views.BookDetail.as_view(), name="bookdetail"),


    # path("error/", views.Error.as_view(), name="error"),

]