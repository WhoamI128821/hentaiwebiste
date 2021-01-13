from django.views.generic import TemplateView
from datetime import date
class IndexView(TemplateView):
    template_name = "index.html"
    
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "HEntai"
        return ctxt
        
class AboutView(TemplateView):
    template_name = "about.html"
    
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        age = date.today()-date(1990,12,8)
        ctxt["dysbth"] = age.days
        return ctxt