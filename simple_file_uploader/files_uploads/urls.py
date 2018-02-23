from django.conf.urls import url

from . import views

app_name = 'files_uploads'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.FileUploadedListView.as_view(),
        name='file-list'
    ),
]
