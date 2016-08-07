import os
from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.template import Template
from django.utils._os import safe_join

# following code taken from http://shop.oreilly.com/product/0636920032502.do


def get_page_or_404(name):
    """Return page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')
    with open(file_path, 'r') as f:
        page = Template(f.read())
    return page


def get_markdown_or_404(name):
    """Return page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')
    with open(file_path, 'rb') as f:
        text = f.read()
    return text


def page(request, slug='index'):
    """Render the requested page if found."""
    file_name = '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    context = {
        'slug': slug,
        'page': page,
    }
    return render(request, 'staticblog/page.html', context)


def markdown(request, slug):
    """Render the requested page if found."""
    file_name = '{}.md'.format(slug)
    text = get_markdown_or_404(file_name)
    context = {
        'slug': slug,
        'text': text,
    }
    return render(request, 'staticblog/markdown.html', context)