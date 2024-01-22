from django_components import component

@component.register("specialists_list")
class Specialists_list(component.Component):
    template_name = "specialists_list/template.html"

    def get_context_data(self):
        return {
            "param": "sample value",
        }

    class Media:
        css = "specialists_list/style.css"
        js = "specialists_list/script.js"