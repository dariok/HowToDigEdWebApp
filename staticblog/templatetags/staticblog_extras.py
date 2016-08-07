import os
from django import template
from django.conf import settings

register = template.Library()
files = os.listdir(settings.SITE_PAGES_DIRECTORY)


@register.inclusion_tag('staticblog/links_to_blogposts.html')
def blogs_navbar():
    filenames = [os.path.splitext(x)[0] for x in files]
    return {"sumsis": filenames}
