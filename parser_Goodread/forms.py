from django import  forms
from . import models, GoodReadParser, parser_GoodRead

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('GoodReads', 'Goodreads'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'GoodRead':
            file_GoodRead = parser_Goodread.parsing()
            for i in file_GoodRead:
                models.GoodReadParser.objects.create(**i)


