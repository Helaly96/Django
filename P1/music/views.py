from django.views import generic
from django.views.generic import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.views.generic import View
from .models import  Album
from .forms import UserForm



from models import Album,Song

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = "all_albums"
    def get_queryset(self):
        return Album.objects.all()



class DetailView(generic.DetailView):

    #eh how el object elly ana 3awez abayen el details bta3to, el object bta3i howa Album hena
    model = Album
    #eh esm el template elly ana 3awez azher el details feha!
    template_name = "music/details.html"

class AlbumCreate(generic.CreateView):
    model = Album
    fields = ["artist","album_title","genre","album_logo"]

#create view de el hadf menha eni a-create an object, w 3lshan a7ot el attributes w 3lshan ad5al el fields
#b7tag 7aga esmaha forms, w howa mn 3'er ma b2olo el template biro7 l album_form
#then ba3d keda goa de el mafrod a7ot el form bs 3amlt template bara 3lshan ashl


class AlbumUpdate(generic.UpdateView):
    model = Album
    fields = ["artist","album_title","genre","album_logo"]




class AlbumDelete(generic.DeleteView):
    model = Album
    success_url = reverse_lazy("music:index")
    #el satr dah by2olo lma tems7 tro7 fen, yro7 yntak.


class UserFormView (View):

    form_class=UserForm
    template_name="music/registeration_form.html"

    def get(self,request):
        form= self.form_class(None)
        return render(request,self.template_name,{"form":form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect("music:index")

        return render(request, self.template_name, {"form": form})


































# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.http import HttpResponse
# from django.http import Http404
# from django.shortcuts import  render
#
# from .models import Album,Song
# from django.template import loader
# from django.shortcuts import render,get_object_or_404
#
#
# # Create your views here.
# def index(request):
#
#     all_albums=Album.objects.all()
#     #hiro7 ygeb el template mn el makan dah  template = loader.get_template("music/index.html")
#
#     #context de el data elly hst5dmha fl HTML
#     context = {"all_albums":all_albums}
#
#
#
#     #by2olo ro7 w render el data de henak!
#     return render(request,"music/index.html",context)
#
#
# def details(request,album_id):
#     #   album=Album.objects.get(pk=album_id)
#
#     album= get_object_or_404(Album,pk=album_id)
#     #el satr elly fo2 dah badal el 404 (try and except)
#     return render(request,"music/details.html",{"album":album})
#
# def favourite (request,album_id):
#     album = get_object_or_404(Album, pk=album_id)
#
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#
#     except(KeyError,Song.DoesNotExist):
#         return render(request,"music/details.html",{"album":album, "error_message":"You didn't select a proper song"})
#
#     else:
#         selected_song.is_favourite=True
#         selected_song.save()
#         return render(request,"music/details.html",{"album":album})
#     #the input is the button, the label is the name next to it.
#     #check Video 24 tani bta3 Buckey
#
#
#



