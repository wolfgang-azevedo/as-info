#!/usr/bin/env python3.8
"""
Project: GetBGP Info
Developed by: Wolfgang Azevedo 
Github: https://github.com/wolfgang-azevedo
Version: 20200218.1
Description: Script to get AS number, prefix, as owner and country from a given IP 
on BGP View API
"""
import requests
import json

class GetBGPInfo:

    def __init__(self, ip_addr):

        self.ip_addr = str(ip_addr)
    
    def get_asnumber(self):

        url = 'https://api.bgpview.io/ip/'

        r = requests.get(f'{url}{self.ip_addr}')
        
        if r.status_code == 200:
            
            result = json.loads(r.text)
            
            prefix = result['data']['prefixes'][0]['prefix']
            as_number = int(result['data']['prefixes'][0]['asn']['asn'])
            as_owner = result['data']['prefixes'][0]['asn']['name']
            country_code = result['data']['prefixes'][0]['asn']['country_code']

            return (f'Prefix: {prefix}\nAS Number: {as_number}\nAS Owner: {as_owner}\nCountry: {country_code}')

        else:
            print("URL não acessível, vericar se o link está disponível")