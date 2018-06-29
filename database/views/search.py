from haystack.query import SearchQuerySet
from haystack.generic_views import SearchView
from haystack.forms import SearchForm


class GeneralSearch(SearchView):
    template_name = 'search/general-search.html'
    form_class = SearchForm

    def get_queryset(self):
        queryset = super(GeneralSearch, self).get_queryset()
        if self.request.method == 'GET':
            params = self.request.GET
            if params.get('q', default=False):
                queryset = SearchQuerySet().filter(text__fuzzy=params['q'])
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(GeneralSearch, self).get_context_data(*args, **kwargs)
        context['size'] = len(self.get_queryset())
        context['object_list'] = self.get_queryset().load_all()
        return context