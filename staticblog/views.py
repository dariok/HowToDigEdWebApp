import os
import markdown2
from django.shortcuts import render
from django.conf import settings
from django.http import Http404, HttpResponseNotFound
from django.template import Template
from django.utils._os import safe_join


def get_matching_extension(slug):
    """ checks if a there is file stored matching the string passed to the function """
    candidates = []
    for x in os.listdir(settings.SITE_PAGES_DIRECTORY):
        if slug == os.path.splitext(x)[0]:
            candidates.append(x)
    if len(candidates) == 1:
        fileinfo = {
            "slug": os.path.splitext(candidates[0])[0],
            "extension": os.path.splitext(candidates[0])[1],
            "filename": slug + os.path.splitext(candidates[0])[1]
        }
    else:
        fileinfo = {
            "slug": "nothing found",
            "extension": "nothing found",
            "filename": slug
        }
    return fileinfo


# some parts of the code was taken from http://shop.oreilly.com/product/0636920032502.do


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
        html = markdown2.markdown(text, extras=["fenced-code-blocks"])
    return html


def page(request, slug='index'):
    """Render the requested page if found."""
    file_name = '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    context = {
        'slug': slug,
        'page': page,
    }
    return render(request, 'staticblog/page.html', context)


def render_static_page(request, slug):
    """Render the requested page if found."""
    fileinfo = get_matching_extension(slug)
    if fileinfo["extension"] in [".md", ".txt"]:
        context = {
            'slug': slug,
            'text': get_markdown_or_404(fileinfo["filename"]),
        }
        return render(request, 'staticblog/markdown.html', context)

    elif fileinfo["extension"] == ".html":
        context = {
            'slug': slug,
            'page': get_page_or_404(fileinfo["filename"]),
        }
        return render(request, 'staticblog/page.html', context)

    elif fileinfo["extension"] == ".xml":
        context = {
            'slug': slug,
            'page': get_page_or_404(fileinfo["filename"]),
        }
        return render(
            request, 'staticblog/xml_template.html', context, content_type='application/xhtml+xml'
        )

    else:
        return HttpResponseNotFound(
            '<h1>A file named "{}" was not found</h1>'.format(fileinfo["filename"])
        )
