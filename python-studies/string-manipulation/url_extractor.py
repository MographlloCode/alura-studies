import re

class UrlExtractor:
    def __init__(self, url):
        ''' Saves the url in a atribute of the object (self.url = url) and verifies if it is valid '''
        self.url = self.url_sanitize(url)
        self.url_validate()

    def url_sanitize(self, url):
        ''' Return the url removing the blank spaces '''
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def url_validate(self):
        ''' Validates if the url is empty '''
        if not self.url:
            raise ValueError('The url is empty.')
        
        url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = url_pattern.match(self.url)

        if not match:
            raise ValueError('Invalid Url')

    def get_base_url(self):
        ''' Returns the base of the url '''
        interrogation_index = self.url.find('?')
        base_url = self.url[0:interrogation_index]
        return base_url

    def get_url_parameters(self):
        ''' Return the parameters of the url '''
        interrogation_index = self.url.find('?')
        url_parameters = self.url[interrogation_index+1:]
        return url_parameters

    def get_parameter_value(self, search_parameter):
        ''' Return the parameters of the 'search_parameter' '''

        # Set the index of the first letter of searched parameter
        parameter_index = self.get_url_parameters().find(search_parameter)

        # Gather the value index of the searched parameter
        value_index = parameter_index + len(search_parameter) + 1

        # Defines the ampersand (or '&') index
        ampersand_index = self.get_url_parameters().find('&', value_index)

        # The following conditional checks if the parameter value has an ampersand (or &) after itsefl
        # if its false, than the find parameter above represents it as '-1' and the conditional below
        # will print the value till the end of the url, otherwise it will print the value till the '&'
        if (ampersand_index == -1):
            parameter_value = self.get_url_parameters()[value_index:]
        else:
            parameter_value = self.get_url_parameters()[value_index:ampersand_index]
        return parameter_value

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return '\n' + 'Full Url: ' + self.url + '\n' + 'Parameters: ' + self.get_url_parameters() + '\n' + 'Base Url: ' + self.get_base_url()

    def __eq__(self, other):
        return self.url == other.url