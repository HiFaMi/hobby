from django.shortcuts import redirect, render

from posts.serializers.post_create import PostCreateSerializer
from ..models import Post
from ..forms import PostForm

from rest_framework import generics
#
#
# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#
#         if form.is_valid():
#             post = form.save(author=request.user)
#             return redirect('index')
#
#     else:
#         form = PostForm()
#         context = {
#             'form': form,
#         }
#
#     return render(request, 'post/post_create.html', context)


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
