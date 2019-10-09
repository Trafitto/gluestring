from gluestring.main import resolve_mxn, resolve_string

DEFAULT_DICTIONARY = {
    "default": "NA"
}

DEFAULT_DELIMITERS = {
    "start": "{{",
    "end": "}}",
}


class Gluegun:

    def __init__(self, mapping=DEFAULT_DICTIONARY, delimiters=DEFAULT_DELIMITERS):
        self.set_delimiters(delimiters)
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

    def set_delimiters(self, delimiters):
        if type(delimiters is dict):
            if "start" in delimiters and "end" in delimiters:
                self.delimiters = delimiters
            else:
                raise Exception(
                    'Expected a dictionary with "start" and "end" as keys.'
                )
        else:
            raise Exception(
                'Excpected type of delimiters to be a dictionary. Got type {}'.format(
                    type(delimiters))
            )

    def glue_it(self, input_template):
        if type(input_template) is list and type(self.mapping) is list:
            return resolve_mxn(input_template, self.mapping, self.delimiters)
        elif type(input_template) is list and type(self.mapping) is dict:
            return resolve_mxn(input_template, [self.mapping], self.delimiters)
        elif type(input_template) is str and type(self.mapping) is list:
            return resolve_mxn([input_template], self.mapping, self.delimiters)
        elif type(input_template) is str and type(self.mapping) is dict:
            return resolve_string(input_template, self.mapping, self.delimiters)
