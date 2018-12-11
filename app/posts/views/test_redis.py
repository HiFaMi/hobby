
from django.http import JsonResponse
from django_redis import cache

from posts.models import Post


def test_view(request):
    posts = cache.get_or_set('posts', Post.objects.all().value('id', 'content'))
    return JsonResponse(list(posts), safe=False)

