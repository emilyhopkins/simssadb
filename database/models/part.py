"""Define a Part model"""
from django.core.exceptions import ValidationError
from django.db import models

from database.mixins.file_and_source_info_mixin import FileAndSourceInfoMixin
from database.mixins.contribution_info_mixin import ContributionInfoMixin
from database.models.custom_base_model import CustomBaseModel


class Part(FileAndSourceInfoMixin, ContributionInfoMixin, CustomBaseModel):
    """A single voice or instrument in a Section of a Musical Work.

    Purely abstract entity that can manifest in differing versions.
    Must belong to one and only one Section.

    Attributes
    ----------
    Part.written_for : models.ForeignKey
        Reference to the Instrument for which this Part was written

    Parts.section : models.ForeignKey
        Reference to the Section to which this Part belongs

    Part.sources : models.ManyToOneRel
        References to Sources that instantiate this Part

    Part.contributions : models.ManyToOneRel
        References to Contributions objects that describe the contributions
        (and thus the contributors) of this Part

    See Also
    --------
    database.models.CustomBaseModel
    database.models.Section
    database.models.Contribution
    database.models.Instrument
    """
    written_for = models.ForeignKey('Instrument',
                                    related_name='parts',
                                    help_text='The Instrument or Voice '
                                              'for which this Part is '
                                              'written',
                                    on_delete=models.PROTECT,
                                    default='')
    section = models.ForeignKey('Section', on_delete=models.CASCADE,
                                related_name='parts',
                                default="",
                                help_text='The Section to which this Part '
                                             'belongs')

    class Meta(CustomBaseModel.Meta):
        db_table = 'part'

    def __str__(self):
        return self.written_for.__str__() + ' part of ' + \
               self.section.__str__() + ' in ' + self.musical_work().__str__()

    def clean(self) -> None:
        """Ensure that only Sections with no children have parts

        Raises
        ------
        ValidationError
            If the Section being validated has child sections and also has Parts
        """
        if self.section.is_node or self.section.is_root:
            raise ValidationError('Only Sections with no children can have '
                                  'Parts')

    def musical_work(self):
        """Get the MusicalWork to which this Part belongs."""
        return self.section.musical_work
