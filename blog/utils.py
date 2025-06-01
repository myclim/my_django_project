from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from blog.models import BlogModel



def post_search(query):
    """Функция поиска товаров по текстовому запросу"""

    if query.isdigit():
        if len(query) < 5:
            return BlogModel.objects.filter(pk=int(query))
        else:
            return BlogModel.objects.none()

    if len(query) < 4:
        return BlogModel.objects.none()

    vector = SearchVector('blog_title', 'description')
    query = SearchQuery(query)

    result = BlogModel.objects.annotate(
        rank=SearchRank(vector=vector, query=query,)).filter(rank__gt=0).order_by("-rank")
    return result
