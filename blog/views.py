from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#def indexView(request):
#    return render(request, 'base.html')

class indexView(ListView):
    model = Post
    template_name = 'index.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ['title', 'body']  # Exclude 'author' field from the form explicitly

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)
    
class PostEditView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    