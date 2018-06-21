from django.db import models
from database.models.custom_base_model import CustomBaseModel
from django.contrib.postgres.fields import ArrayField
from database.models.genre import Genre
from database.models.section import Section
from django.urls import reverse


class MusicalWork(CustomBaseModel):
    """A complete work of music

    A purely abstract entity that can manifest in differing versions.
    Divided into sections.
    Must have at least one section.
    """
    variant_titles = ArrayField(
                    models.CharField(max_length=200, blank=True),
                    blank=False, null=False, default=['hello', 'world'])

    genres_as_in_style = models.ManyToManyField(Genre,
                                                related_name='style')
    genres_as_in_form = models.ManyToManyField(Genre,
                                               related_name='form')

    sections = models.ManyToManyField(Section, related_name='in_works')
    religiosity = models.NullBooleanField(null=True, blank=True, default=None)
    viaf_url = models.URLField(null=True, blank=True)
    other_authority_control_url = models.URLField(null=True, blank=True)
    contributors = models.ManyToManyField(
                                        'Person',
                                        through='ContributedTo',
                                        through_fields=(
                                            'contributed_to_work', 'person')
                                          )

    @property
    def composers(self):
        composers = []
        relationships = self.contributed_to.filter(role='COMPOSER')
        for relationship in relationships:
            composers.append(relationship.person)
        return composers
        
    def __str__(self):
        return "{0}".format(self.variant_titles[0])

    def get_absolute_url(self):
        return reverse("musicalwork_detail", kwargs={'pk': self.pk})

    class Meta(CustomBaseModel.Meta):
        db_table = 'musical_work'
