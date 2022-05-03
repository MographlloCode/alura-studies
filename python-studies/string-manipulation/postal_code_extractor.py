# Regular expressions or Re
import re 

# Setting the address
address = 'Rua das FLores 72, aparamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'

# Brazilian postal code has the following pattern = 5 digits + hiphen + 3 digits

pattern = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
search = pattern.search(address) # Match or None

if search:
    postal_code = search.group()
    print(postal_code)