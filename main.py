import requests, sys, os, inquirer
from dotenv import load_dotenv
import xml.etree.ElementTree as ET

load_dotenv()

def search_movie(*args):
    movie_name = " ".join(args)
    apikey = os.getenv('apikey')
    url = f"http://omdbapi.com/?apikey={apikey}&t={movie_name}"

    result = requests.get(url)

    if result.status_code == 200:
        return result.json()
    else:
        print("Request gelmedi")
        exit()

def search_book(*args):
    book_name = " ".join(args)
    apikey = '5OVwGm0ylIwc1aSv8PamQ'
    url = f"https://www.goodreads.com/search/index.xml?key={apikey}&q={book_name}"

    result = requests.get(url)
    root = ET.fromstring(result.text)

    for book in root.iter('work'):
        print('\nBook ID: ' + book[0].text)
        print('Book name: "' + book[8][1].text + '"')
        print('Author: ' + book[8][2][1].text)
        print('Rating: ' + book[7].text)
        print("----------------------------------------")

if len(sys.argv) < 3:
    print("Alinmadi")
    exit()
else:
    if sys.argv[1] == 'movie':
        result = search_movie(*sys.argv[2:])
        # if result['Response'] == 'False':
        #     print(result['Error'])
        #     exit()
        # else:
        print(result)
            # print('Title: ', result['Title'])
            # print('Year: ', result['Year'])
            # print('Released: ', result['Released'])
    elif sys.argv[1] == 'book':
        result = search_book(*sys.argv[2:])
