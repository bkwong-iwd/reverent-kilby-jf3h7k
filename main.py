# arparse is only needed if we want to run specific methods from command line, otherwise can just invoke methods and click Replit Run
# import argparse

# first run `pip install requests wptools` in the terminal
import requests
import wptools

### Additional Resources
# tests and mocking: https://realpython.com/python-mock-library/#what-is-mocking 
#. to mock our HTTP request (see https://docs.python.org/3/library/unittest.mock.html#patch-object)
#.    - to mock responses: https://docs.python.org/3/library/unittest.mock.html#the-mock-class
# requests docs: https://requests.readthedocs.io/en/latest/user/quickstart/ for making HTTP requests
# wptools docs: https://github.com/siznax/wptools

# Step 1 - make a GET request to Gutendex API
# Step 2 - write unit tests - see bookservice_test.py; 
#   in the terminal, run `python bookservice_test.py`
class BooksService():
    def search_books_by_artist(author:str) -> list:
        url=f"https://gutendex.com/books/?search={author}"
        response = requests.get(url)
        if response.status_code == 200 and response.json():
            return response.json()
        else:
            return None

# Step 3 - using wptools lib, get Wiki info from the MediaWiki API. 
#   Then write tests. See `mediawikiservice_test.py`
class MediaWikiService():
    def get_infobox(title:str):
        page = wptools.page(title) # retrieve/create a page object
        try:
          page.get_parse() # parse the page data
          if page.data['infobox'] is not None:
              # if infobox is present
              infobox = page.data['infobox']
              return infobox
              # get data for the interested features/attributes
              # data = { feature : infobox.get(feature, "") for feature in features }
          else:
              print("No infobox found")
              # data = { feature : '' for feature in features }
              pass

        except Exception as e:
            print("Something went wrong: ", e)
            pass

# Step 4 - Main Function that calls both of the above methods (get book, then retrieve wiki info) and returns our own object
# Step 5 - Write tests, see `main_test.py`
def main():
    books = BooksService.search_books_by_artist("Bram Stoker").get('results')

    book_details = {}
    limit = 10 if len(books) > 10 else len(books) # arbitrarily limit the number of times we call the MediaWiki API to max 10

    if books:
        for i in range(0, limit):
            book = books[i]
            book_wiki_info = MediaWikiService.get_infobox(title=book['title'])
            # wiki_infos.append(book_wiki_info)

            if book_wiki_info:
                book_details[book['title']] = {
                    'release_date': book_wiki_info.get('release_date'),
                    'pages': book_wiki_info.get('pages')
                }
    
    print(book_details)
    return book_details;

main()

# This part is only needed if we want to run specific methods directly from command line instead of invoking main() in the code - i.e. python main.py main
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description="Execute a function in the script.")
#     parser.add_argument("method", help="The method to execute (greet or add)")
#     args = parser.parse_args()

#     if args.method == "main":
#   

