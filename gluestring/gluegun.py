from gluestring.main import resolve_mxn, resolve_string
from gluestring.default import DEFAULT_DICTIONARY, DEFAULT_DELIMITERS, DEFAULT_OPTIONS


class Gluegun:
    options = {}
    def __init__(self, mapping=DEFAULT_DICTIONARY, options=DEFAULT_OPTIONS):

        self.set_options(options)

        if (type(mapping) is dict):
            self.mapping = {**DEFAULT_DICTIONARY, **mapping}
        elif (type(mapping) is list):
            defaulted_mapping_list = []
            for dictionary in mapping:
                defaulted_mapping_list.append(
                    {**DEFAULT_DICTIONARY, **dictionary}.copy())
            self.mapping = defaulted_mapping_list
        else:
            raise Exception(
                'Excpected type of mapping to be a dictionary or a list of dictionary. Got type {}'.format(type(mapping)))

    def set_delimiters(self, options):
        delimiters = options.get("delimiters", None)
        if type(delimiters is dict):
            if "start" in delimiters and "end" in delimiters:
                self.options['delimiters'] = delimiters
            else:
                raise Exception(
                    'Expected a dictionary with "start" and "end" as keys.'
                )
        else:
            raise Exception(
                'Excpected type of delimiters to be a dictionary. Got type {}'.format(
                    type(delimiters))
            )

    def set_options(self, options):
        if type(options) is dict:
            self.options = options

            if "delimiters" not in options:
                self.options['delimiters'] = DEFAULT_DELIMITERS
            else:
                self.set_delimiters(options)

        else:
            raise Exception(
                'Excpected type of options to be a dictionary. Got type {}'.format(
                    type(options))
            )
        

    def glue_it(self, input_template):
        if type(input_template) is list and type(self.mapping) is list:
            return resolve_mxn(input_template, self.mapping, self.options)
        elif type(input_template) is list and type(self.mapping) is dict:
            return resolve_mxn(input_template, [self.mapping], self.options)
        elif type(input_template) is str and type(self.mapping) is list:
            return resolve_mxn([input_template], self.mapping, self.options)
        elif type(input_template) is str and type(self.mapping) is dict:
            return resolve_string(input_template, self.mapping, self.options)
