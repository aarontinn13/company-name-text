import requests
import clearbit


clearbit.key = 'sk_6a79cb6eb22caf2e9478c3fc74cebf44'

url = ('https://company.clearbit.com/v1/domains/find?name=')

response1 = requests.get(url, auth=(clearbit.key,'pass'))
#print(response1)

response1 = response1.json()

print(response1)


