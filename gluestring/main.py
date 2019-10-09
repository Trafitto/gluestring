import re


def _get_regex_delimiter(values):
    delimiter = ""
    for value in values:
        delimiter += f"\{value}"
    return delimiter

def resolve_string(templateString, dictionaryToMatch, delimiters):

    pattern = re.compile(r'{start}([^{not_match}$]*){end}'.format(
        start=_get_regex_delimiter(delimiters['start']),
        not_match=delimiters['end'][0],
        end=_get_regex_delimiter(delimiters['end'])
    ))
    number_of_patterns_found = len(pattern.findall(templateString))
    for _ in range(number_of_patterns_found):
        val = pattern.search(templateString).groups()[0]
        if val.strip() in dictionaryToMatch:
            templateString = templateString.replace(
                delimiters["start"]+val+delimiters["end"],
                str(dictionaryToMatch[val.strip()]), 1)
        else:
            templateString = templateString.replace(
                delimiters["start"]+val+delimiters["end"],
                str(dictionaryToMatch['default']), 1)
    return templateString

# def resolve_list(templateStringList, dictionaryToMatch ):
#     for templateString in templateStringList:


def resolve_mxn(templateStringList, dictionaryToMatchList, delimiters):
    result = []
    for templateString in templateStringList:
        for dictionaryToMatch in dictionaryToMatchList:
            result.append(resolve_string(templateString,
                                         dictionaryToMatch, delimiters))
    return result
