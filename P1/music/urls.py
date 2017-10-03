from django.conf.urls import url
from . import views

app_name ="music"
#de ht5lini ast5dm el name fe kaza makan msh fl app dah bas
#ya3ni a2dar asami details masln fe app tani 3'er el music


urlpatterns = [

    # dah el home page bta3et el music app
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^register/$', views.UserFormView.as_view(), name="register"),

    #(?P<album_id>[0-9]+) : el 2 brackets de bt2olo 3amel kol elly goa k2enhom nafs el 7aga msh seperate
    # el ?P de bt2olo e3mal variable bl esm elly goa el tags deeeee
    #[0-9]+ de bt2olo en dah hyb2a integers w + de bt2olo eno aktr mn just a one number


    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="details"),
    # url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name="favourite"),

    url(r'^album/add/$', views.AlbumCreate.as_view(), name="album-add"),

    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name="album-update"),

    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name="album-delete"),


]
