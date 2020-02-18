#!/usr/bin/env python3.8
"""
Project: GetBGP Info
Developed by: Wolfgang Azevedo 
Github: https://github.com/wolfgang-azevedo
Version: 20200218.1
Description: Script to get AS number, prefix, as owner and country from a given IP 
on BGP View API
"""

from get_as_info import GetBGPInfo
import argparse
import logging

parser = argparse.ArgumentParser() #Instanciado o método ArgumentParser

parser.add_argument("-i", "--ip", help="Enter the IP Address")

if __name__ == "__main__":

    args = parser.parse_args()
    
    if args.ip:
        
        r = GetBGPInfo(args.ip)
        print(r.get_asnumber())
