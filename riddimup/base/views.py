from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView
from users.models import Comment, Track
from users.forms import CommentForm
from django.http import JsonResponse
from django.db.models import Q


# Create your views here.
def home(request):
    user = request.user
    context = {
        'user': user,
        'tracks': Track.objects.all(),
        'tracks2': Track.objects.order_by("-like_count")[:10]
    }
    return render(request, 'base/home.html', context) 

def charts(request):
    tracks = Track.objects.order_by("-like_count")[:10]
 
    context = {
        'tracks': tracks 
    }
    return render(request, 'base/charts.html', context)


class TrackDetailView(DetailView):
    template_name = 'track.html'
    model = Track
    context_object_name = 'track'

    form = CommentForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context
    
    def post(self, request, slug):
        form = CommentForm(request.POST)
        track = self.get_object()
        if form.is_valid():
            form.instance.author = request.user
            form.instance.track = track
            form.save()

            return redirect(reverse("track", kwargs={
                'slug': track.slug 
            }))
        else:
            return redirect(reverse("track", kwargs={
                'slug': track.slug 
            }))
    
    
  

@login_required
def like(request):
    if request.method == 'POST':
        result = ''
        id = request.POST.get('trackid')
        track = get_object_or_404(Track, id=id)

        if track.likes.filter(id=request.user.id).exists():
            track.likes.remove(request.user)
            track.like_count -= 1
            result = track.like_count
            track.save()
        else:
            track.likes.add(request.user)
            track.like_count += 1
            result = track.like_count
            track.save()

        return JsonResponse({'result': result,})

def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        tracks = Track.objects.filter(Q(track_title__icontains=searched) | Q(artist_name__icontains=searched))

        context = {
            'searched': searched,
            'tracks': tracks
        }
         
        return render(request, 'base/search.html', context)

    else:  
        return render(request, 'base/search.html')
