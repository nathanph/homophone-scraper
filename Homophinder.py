__author__ = 'Nathan Hernandez'

from bs4 import BeautifulSoup
import requests
import re
import string


def main():
    # Test page to parse.
    page = requests.get('http://www.homophone.com/search?type=begin&q=A')
    # Grab the HTML.
    data = page.text

    # Have BeautifulSoup parse the HTML.
    soup = BeautifulSoup(data)

    # Grab the <h5> tag text (it should contain "Page # / #").
    pages = soup.h5.text

    # Use RegEx to match the first and second number.
    page_match = re.match(r'Page ([0-9]+) / ([0-9]+)', pages)

    if page_match:
        current_page = page_match.group(1)
        last_page = page_match.group(2)
        print("Current page: ", current_page)
        print("Last page: ", last_page)
    else:
        print("No match")

    extra_code()

def extra_code():
    # Loop through each character a-z.
    for char in string.ascii_lowercase:
        print(char)

if __name__ == "__main__":
    main()
