from django.http import HttpResponse
from . import models, forms
from django.views import generic

class GoodReadListView(generic.ListView):
    template_name = 'parser/GoodRead_list.html'
    context_object_name = 'GoodRead'
    model = models.GoodReadParser

    def get_queryset(self):
        return self.model.objects.all()

class GoodReadFormView(generic.FormView):
    template_name = 'parser/GoodRead_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Парсинг успешно завершен')
        else:
            return super(GoodReadFormView, self).post(request, *args, **kwargs)





