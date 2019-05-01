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
        print("Bad request")
        exit()

def search_book(*args):
    book_name = " ".join(args)
    apikey = '5OVwGm0ylIwc1aSv8PamQ'
    url = f"https://www.goodreads.com/search/index.xml?key={apikey}&q={book_name}"

    result = requests.get(url)
    root = ET.fromstring(result.text)

    book_arrey = [[book[0].text, book[8][1].text, book[8][2][1].text, book[7].text] for book in root.iter('work')]

    if int(next(root.iter('total-results')).text) > 0:
        return book_arrey
    else:
        print("Bad request")
        exit()

if len(sys.argv) < 3:
    print("Wrong input")
    exit()
else:
    if sys.argv[1] == 'movie':
        result = search_movie(*sys.argv[2:])
        if result['Response'] == 'False':
            print(result['I cant find this movie. '])
            exit()
        else:
            print("----------------------------------------")
            print('Title: ', result['Title'])
            print('Year: ', result['Year'])
            print('Released: ', result['Released'])
            print('Genre: ', result['Genre'])
            print('Director: ', result['Director'])
            print("----------------------------------------")

    elif sys.argv[1] == 'book':
        result = search_book(*sys.argv[2:])

        print("----------------------------------------")
        for i in range(3):
            print('Book ID: ' + result[i][0])
            print('Book name: "' + result[i][1] + '"')
            print('Author: ' + result[i][2])
            print('Rating: ' + result[i][3])
            print("----------------------------------------")