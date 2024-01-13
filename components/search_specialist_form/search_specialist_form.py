from django_components import component

@component.register("search_specialist_form")
class Search_specialist_form(component.Component):
    template_name = "search_specialist_form/template.html"

    class Media:
        css = "search_specialist_form/style.css"
        js = "search_specialist_form/script.js"