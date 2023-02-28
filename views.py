from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.http import HttpResponseRedirect


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    # ordering = ['-id']
    ordering = ['-created_at']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class ArticalView(DetailView):
    model = Post
    template_name = "blogpost.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticalView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id= self.request.user.id).exists():
            liked = True
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddBlog(CreateView):
    model = Post
    form_class = PostForm
    template_name = "Add_blog.html"
    # fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddBlog, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class Addcategory(CreateView):
    model = Category
    template_name = "Add_category.html"
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Addcategory, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def categoryView(request, cats):
    category_post = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'Categroies.html', {'cats': cats.title().replace('-', ' '), 'category_post': category_post})


class UpdateBlog(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdateBlog, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class DeleteBlog(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeleteBlog, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blogpost', args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'Add_comments.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')

     
