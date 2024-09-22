# Ich weiß wo dein Internetprovider wohnt (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/requests/001/)

import requests

if __name__ == '__main__':
  responses = requests.get('https://api.ipify.org')
  print(f'Your ip: {responses.text}')
