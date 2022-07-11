from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Articles


class Index(TemplateView):
    template_name = 'index.html'
    model = Articles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["lista"] = self.model.objects.all()
        for i in context["lista"]:
            print(i)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)