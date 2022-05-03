from url_extractor import *

url_extractor = UrlExtractor('https://www.bytebank.com/cambio?moedaDestino=real&quantidade=100&moedaOrigem=dolar')

dolar_value_in_real = 5.50 # $1 = R$5.50
currency_of_origin = url_extractor.get_parameter_value('moedaOrigem').lower()
currency_of_destination = url_extractor.get_parameter_value('moedaDestino').lower()
ammount = int(url_extractor.get_parameter_value('quantidade'))

if (currency_of_origin == 'real' and currency_of_destination == 'dolar'):
    exchange = ammount / dolar_value_in_real
    print(f'R${ammount:.2f} to Dolar($): {exchange:.2f}')
elif (currency_of_origin == 'dolar' and currency_of_destination == 'real'):
    exchange = ammount * dolar_value_in_real
    print(f'${ammount:.2f} to Real(R$): {exchange:.2f}')
else:
    print(f'The exchange of {currency_of_origin} to {currency_of_destination} is not available yet.')
