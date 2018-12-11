from django.shortcuts import redirect, render

from ..forms import PostForm


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(author=request.user)
            return redirect('index')

    else:
        form = PostForm()
        context = {
            'form': form,
        }

    return render(request, 'post/post_create.html', context)
