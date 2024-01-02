import sys
import requests
import json

def main():
    # We start a loop
    while True:
        # Try to do this
        try:
            # If length is too short
            if len(sys.argv) < 2:
                sys.exit("Missing command-line argument")
            # We turn second argument into a float
            times = float(sys.argv[1])
            # We use requests to get our api and assign it it a variable
            bitapi = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            # We decode the api into json format
            o = bitapi.json()
            # We browse through the api for the rate_float, inside USD, inside bpi, and make sure it is a float
            rate = float(o["bpi"]["USD"]["rate_float"])
            # We get the amount we want to output, by multiplying the rate by the system argument
            amount = rate * times
            # Then we print it out formatted
            print(f"${amount:,.4f}")
            # Break because we are successful
            break
        # If the sys argument is not a number
        except ValueError:
            sys.exit("Command-line argument is not a number")

main()