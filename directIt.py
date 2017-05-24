"""
This is a adaptation of the mapIt.py exercise from the Automate The Boring Stuff Book. Where that exercise was to pull one address, this fork takes in two addresses and maps directions.
"""
import webbrowser, sys
from_addy = input("What address are you starting from? ")
to_addy = input("What address do you want directions to? ")

webbrowser.open('https://www.google.com/maps/dir/' + from_addy + '/' + to_addy + '/')