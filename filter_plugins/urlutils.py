from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from urlparse import parse_qs, urljoin

def parse_url_query_string(query_string):
    """returns a dictionary of the parsed elements of a URL query string component"""

    return dict( (k, v if len(v) > 1 else v[0] )
        for k, v in parse_qs(query_string).iteritems() )


def query_string(query_dict):
    """returns the URL query string representation of a dictionary"""
    return ';'.join("%s=%s" % (key,val) for (key,val) in query_dict.iteritems())


def urlsplit_split_query(urlsplit_value):
    """given the dictionary returned by the urlsplit filter parses the query key into a dictionary"""
    urlsplit_value['query'] = parse_url_query_string(urlsplit_value['query'])

    return urlsplit_value


def url_combine(split_url):
    """composes a URL from a dictionary using the same keys as produced by the urlsplit filter"""
    result = ""

    if split_url["scheme"]:
        result = "{}:".format(split_url["scheme"])
    if split_url["hostname"]:
        result = "{}//{}".format(result, split_url["hostname"])
    if split_url["port"]:
        result = "{}:{}".format(result, split_url["port"])
    if split_url["path"]:
        result = "{}{}".format(result, split_url["path"])
    if split_url["query"]:
        if type(split_url["query"]) is dict:
            result = "{}?{}".format(result, query_string(split_url["query"]))
        else:
            result = "{}?{}".format(result, split_url["query"])
    if split_url["fragment"]:
        result = "{}#{}".format(result, split_url["fragment"])

    return result


class FilterModule(object):
    def filters(self):
        return {
            "urlsplit_splitquery": urlsplit_split_query,
            "urlcombine": url_combine
        }
