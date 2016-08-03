# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2016 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints full-text URLs
"""

from urllib import quote_plus


def format_element(bfo, style, separator=', '):
    """
    This is the default format for formatting full-text URLs.
    @param separator: the separator between urls.
    @param style: CSS class of the link
    """

    urls = bfo.fields("710__g")

    urls = ['<a href="/search?p=collaboration:%27' + quote_plus(url) + '%27">'
            + url +'</a>' for url in urls]
    return separator.join(urls)


# pylint: disable=W0613
def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
# pylint: enable=W0613
