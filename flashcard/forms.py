from django.views.generic.edit import UpdateView
from manageset.models import WordMeanings

class WordMeaningUpdate(UpdateView):
    model = WordMeanings
    fields = ['word']
    # template_name_suffix = '_update_form'