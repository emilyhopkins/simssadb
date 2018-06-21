from django.views.generic import (TemplateView, CreateView)
from drf_haystack.viewsets import HaystackViewSet
from . import forms
from django.urls import reverse
from database.serializers import *
from rest_framework import viewsets
from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet


class HomeView(TemplateView):  # show about page
    template_name = 'home.html'


class AboutView(TemplateView):  # show about page
    template_name = 'about.html'


class SignUp(CreateView):
    form_class = forms.UserCreateForm

    def get_success_url(self):
        return reverse('login')
    # success_url = reverse('about.html')  # cause "circular import" problem
    template_name = "registration/signup.html"


class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class GeographicAreaViewSet(viewsets.ModelViewSet):
    queryset = GeographicArea.objects.all()
    serializer_class = GeographicAreaSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class MusicalWorkViewSet(viewsets.ModelViewSet):
    queryset = MusicalWork.objects.all()
    serializer_class = MusicalWorkSerializer


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class PersonSearchView(HaystackViewSet):
    index_models = [Person]
    serializer_class = PersonSearchSerializer


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class CollectionOfSourcesViewSet(viewsets.ModelViewSet):
    queryset = CollectionOfSources.objects.all()
    serializer_class = CollectionOfSourcesSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class GeneralSearch(SearchView):

    def get_queryset(self):
        print('***' * 30)
        if self.request.GET['models']:
            sqs = SearchQuerySet().filter(text__fuzzy=self.request.GET[
                'q']).models(self.request.GET['models'])
        else:
            sqs = SearchQuerySet().filter(text__fuzzy=self.request.GET['q'])
        for result in sqs:
            print(result.object)
        return sqs
    context_object_name = 'results'
    template_name = 'search/search.html'
