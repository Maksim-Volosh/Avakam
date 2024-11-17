from django import template

register = template.Library()

@register.simple_tag()
def nextpage(request):
    if request.GET.get('next'):
        return f"?next={request.GET.get('next')}"
    else:
        return ""
