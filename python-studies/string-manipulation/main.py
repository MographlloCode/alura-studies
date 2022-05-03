# Full url
url = 'bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'

# Url Sanitizing
url = url.replace(' ', '')

# Url Validation
if (url == ''):
    pass


# Separates base and parameters
interrogation_index = url.find('?')
base_url = url[0:interrogation_index]
url_parameters = url[interrogation_index+1:]

print (f'Url: {url}')
print (f'Base: {base_url}')
print (f'Parameters: {url_parameters}')

# Defines search parameters
search_parameter = 'moedaDestino'

# Set the index of the first letter of searched parameter
parameter_index = url_parameters.find(search_parameter)

# Gather the value index of the searched parameter
value_index = parameter_index + len(search_parameter) + 1

# Defines the ampersand (or '&') index
ampersand_index = url_parameters.find('&', value_index)

# The following conditional checks if the parameter value has an ampersand (or &) after itsefl
# if its false, than the find parameter above represents it as '-1' and the conditional below
# will print the value till the end of the url, otherwise it will print the value till the '&'
if (ampersand_index == -1):
    parameter_value = url_parameters[value_index:]
    print(parameter_value)
else:
    parameter_value = url_parameters[value_index:ampersand_index]
    print(parameter_value)