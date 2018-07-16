from django.db import models
from database.models.file import File
from database.models.source import Source
from database.models.instrument import Instrument
import os


class SymbolicMusicFile(File):
    """
    Manifestation of a Musical Instance as a digital music file

    Generated from a Source by a Symbolic Encoder
    """
    instruments_used = models.ManyToManyField(Instrument,
                                              help_text='The Instruments used '
                                                        'in this Symbolic File')

    manifests = models.ForeignKey(Source,
                                  related_name='manifested_by_sym_files',
                                  on_delete=models.CASCADE, null=False,
                                  help_text='The Source manifested by this '
                                            'Symbolic File')
    file = models.FileField(upload_to='symbolic_music/',
                            help_text='The actual file')

    def __str__(self):
        filename = os.path.basename(self.file.name)
        return "{0}".format(filename)

    def prepare_summary(self):
        summary = {'display':   self.__str__(),
                   'file_type': self.file_type,
                   'source':    self.manifests.part_of_collection.title,
                   'url':       self.get_absolute_url()
                   }
        return summary

    class Meta:
        db_table = 'symbolic_music_file'
