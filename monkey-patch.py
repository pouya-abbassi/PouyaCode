"""
As the name suggests, this file contains fixes that I need but couldn't do in pelican platform.
Should run this after `make publish`.
"""

import os, re
from shutil import copyfile
from lxml import html
from publishconf import *
from subprocess import call


def modify_url():
    """Adds `rel=nofollow` and `target=_blank` to external urls, mostly used inside blog posts."""
    files = create_list()
    for each in files:
        with open(each, 'r') as f:
            root = html.fromstring(f.read())
            for el in root.iter('a'):
                try:
                    if re.search('^http', el.attrib['href']):
                        if not(re.search('^' + SITEURL ,el.attrib['href'])):
                            el.attrib['rel'] = 'nofollow'
                            el.attrib['target'] = '_blank'
                        #print(html.tostring(root, pretty_print=True))
                except:
                    pass
            f.close()
            with open(each, 'wb') as f:
                f.write(b'<!DOCTYPE html>')
                f.write(html.tostring(root))
                f.close()

        dirpath = '/'.join(each.split('/')[:-1])
        name = each.split('/')[-1]
        optimize(dirpath, name)


def modify_img():
    """Replaces `<p><img></p>' with '<img>'."""
    files = create_list()
    for each in files:
        with open(each, 'r') as f:
            original = f.read()
            find = re.findall('<p><img.+>', original)
            split = re.split('<p><img.+>', original)
            find2 = []
            for substr in find:
                find2.append(substr[3:] + '<p>')
            result = ''
            for substr in find2:
                result += split[find2.index(substr)]
                result += substr
            result += split[-1]
            f.close()
        with open(each, 'w') as f:
            f.write(result)
            f.close()

        dirpath = '/'.join(each.split('/')[:-1])
        name = each.split('/')[-1]
        optimize(dirpath, name)


def create_list():
    """Create list of html files in public directory."""
    walk_dir = 'public'
    walk_dir = os.path.abspath(walk_dir)
    html_list = []

    for root, dirs, files in os.walk(walk_dir):
        for name in files:
            if name.split('.')[-1] == 'html':
                html_list.append(os.path.join(root, name))

    return html_list


def optimize(dirpath, filename):
    """Minifies and standardizes html files after lxml does its job."""
    command = ('minify "{filename}" -o "{filename}"', '--quiet', '')

    filepath = os.path.join(dirpath, filename)

    ext = os.path.splitext(filename)[1]
    command, silent, verbose = command
    flags = silent
    command = command.format(filename=filepath, flags=flags)
    call(command, shell=True)


if __name__ == '__main__':
    create()
    modify_url()
    modify_img()
