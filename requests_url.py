import requests
import clearbit

clearbit.key = 'sk_6a79cb6eb22caf2e9478c3fc74cebf44'

with open('testfile.txt', 'r') as r:
    for line in r:
        url = ('https://company.clearbit.com/v1/domains/find?name={}'.format(line))
        response1 = requests.get(url, auth=(clearbit.key,'pass'))


        response1 = response1.json()

        #currently writing to append
        with open('file2.txt', 'a') as a:
            try:
                a.write(response1['domain'])
                a.write('\n')
            except KeyError:
                a.write('Cannot Find Website')
                a.write('\n')

