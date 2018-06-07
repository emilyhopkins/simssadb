from django.db import models
from database.models.custom_base_model import CustomBaseModel
from django.contrib.postgres.fields import ArrayField
from database.models.genre import Genre
from database.models.section import Section
from database.models.part import Part
from django.contrib.contenttypes.fields import GenericRelation
from database.models.musical_instance import MusicalInstance
from django.urls import reverse


class MusicalWork(CustomBaseModel):
    """A complete work of music

    A purely abstract entity that can manifest in differing versions.
    Divided into sections and parts.
    Must have at least one section and at least one part.
    """
    title = models.CharField(max_length=200, blank=False)
    variant_titles = ArrayField(
            ArrayField(
                    models.CharField(max_length=200, blank=True)
            ),
            blank=True, null=True
    )
    genre_as_in_style = models.ForeignKey(Genre, on_delete=models.SET_NULL,
                                          null=True,
                                          related_name='style')
    genre_as_in_form = models.ForeignKey(Genre, on_delete=models.SET_NULL,
                                         null=True,
                                         related_name='form')

    sections = models.ManyToManyField(Section, related_name='in_works')
    parts = models.ManyToManyField(Part, related_name='in_works')
    instance = GenericRelation(MusicalInstance)


    def get_absolute_url(self):
        return reverse("musicalwork_detail", kwargs={'pk': self.pk})

    class Meta(CustomBaseModel.Meta):
        db_table = 'musical_work'
