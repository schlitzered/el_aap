__author__ = 'schlitzer'

from el_aap_api.errors import *


class ProjectionMixIn(object):
    def _projection(self, fields=None):
        if not fields:
            return self.defaultfields
        fields = fields.split(sep=',')
        for field in fields:
            if field not in self.defaultfields:
                raise InvalidFields('{0} is not a valid field'.format(field))
        result = {}
        for field in fields:
            result[field] = 1
        return result


class FilterMixIN(object):
    @staticmethod
    def _filter_builder_boolean(query, field, selector):
        if not selector:
            return
        if selector in [True, 'true', 'True', '1']:
            selector = True
        elif selector in [False, 'false', 'False', '0']:
            selector = False
        else:
            raise InvalidSelectors('Selector is not a boolean')
        query[field] = selector

    @staticmethod
    def _filter_builder_list(query, field, selector):
        if not selector:
            return
        if type(selector) is not list:
            selector = list(set(selector.split(',')))
        query[field] = {'$in': selector}

    @staticmethod
    def _filter_builder_re(query, field, selector):
        if not selector:
            return
        query[field] = {'$regex': selector}
