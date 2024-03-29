from django_components import component

@component.register("footer")
class Footer(component.Component):
    template_name = "footer/template.html"

    class Media:
        css = "footer/style.css"
        js = "footer/script.js"