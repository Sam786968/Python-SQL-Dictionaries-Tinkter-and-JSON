

# Grabbing public json data.
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/currencies/") as response:
  source = response.read()


# print(source)
with open("source","w") as f:
  f.write(Yahoo_Finance.txt)
  
# print(len(data['list']['resources']))
