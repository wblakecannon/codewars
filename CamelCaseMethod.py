'''
Write simple .camelcase method (camel_case function in PHP) for strings.
All words must have their first letter capitalized without spaces.

For instance:
camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
'''


def camel_case(string):
    string = str.title(string)
    return string.replace(" ", "")


print camel_case("test case")
print camel_case("camel case method")
print camel_case("say hello ")
print camel_case(" camel case word")
print camel_case("")