__author__ = 'Nathan Hernandez'

from bs4 import BeautifulSoup
import requests
import re
import string


def main():
    for char in string.ascii_lowercase:
        # Test page to parse.
        page = requests.get('http://www.homophone.com/search?page=1&q=' + char + '&type=begin')
        # Grab the HTML.
        data = page.text

        # Have BeautifulSoup parse the HTML.
        soup = BeautifulSoup(data)

        # Grab the <h5> tag text (it should contain "Page # / #").
        pages = soup.h5.text

        # Use RegEx to match the first and second number.
        page_match = re.match(r'Page ([0-9]+) / ([0-9]+)', pages)

        #print(str(page) + " in " + char)

        if page_match:
            current_page = page_match.group(1)
            last_page = page_match.group(2)
            #print("Current page: ", current_page)
            #print("Last page: ", last_page)
        #else:
            #print("No match")

        for page in range(1, int(last_page)+1):
            # Test page to parse.
            page = requests.get('http://www.homophone.com/search?page=' + str(page) + '&q=' + char + '&type=begin')
            # Grab the HTML.
            data = page.text

            # Have BeautifulSoup parse the HTML.
            soup = BeautifulSoup(data)

            # Grab the <a> tag text with class "word-btn" (it should contain a homophone).
            words = soup.find_all("a", class_="word-btn")
            #print("Total words: ", len(words))

            for word in words:
                print(word.get_text())

if __name__ == "__main__":
    main()
