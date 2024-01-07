from django_components import component

@component.register("search_bar")
class Search_bar(component.Component):
    template_name = "search_bar/template.html"

    class Media:
        css = "search_bar/style.css"
        js = "search_bar/script.js"