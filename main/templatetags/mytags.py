from django import template
register = template.Library()


@register.simple_tag
def get_lang_url(request, language):
    url = request.path.split('/')
    url[1] = language
    url = '/'.join(url)
    return url
    # url = request.path
    # url = '/' + language + url[3:]
    # return url
