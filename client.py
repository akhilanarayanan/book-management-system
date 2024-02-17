import argparse
import json
import requests

# Function to make a GET request to fetch all books
def get_books(collection_id=None, genre=None, author=None):
  # URL of my API
  base_url = 'http://localhost:5000'
  
  base_url += "/books"
  q_mark_needed = True
  
  if (collection_id):
    base_url += "?collection_id="
    base_url += collection_id
    q_mark_needed = False
  
  if (genre and q_mark_needed):
    base_url += "?genre="
    for word in genre:
      base_url += word
      base_url += " "
    base_url = base_url.rstrip()
    q_mark_needed = False
  elif (genre and not q_mark_needed):
    base_url += "&genre="
    for word in genre:
      base_url += word
      base_url += " "
    base_url = base_url.rstrip()
    base_url += genre
    
  if (author and q_mark_needed):
    base_url += "?author="
    for word in author:
      base_url += word
      base_url += " "
    base_url = base_url.rstrip()
    q_mark_needed = False
  elif (author and not q_mark_needed):
    base_url += "&author="
    for word in author:
      base_url += word
      base_url += " "
    base_url = base_url.rstrip()

  response = requests.get(base_url)
  if response.status_code == 200:
    return response.json()
  else:
    print('Failed to fetch books.')
    return None

def get_collections():
  base_url = 'http://localhost:5000/collections'
  response = requests.get(base_url)
  if response.status_code == 200:
    return response.json()
  else:
    print('Failed to fetch books.')
    return None

def add_collection(name=None):
  if name is None:
    print('Please specify a name for your collection')
    return None

  base_url = 'http://localhost:5000/add_collection'
  nameStr = ''
  for n in name:
    nameStr += n
    nameStr += ' '
  nameStr = nameStr.rstrip()
  data = {'name': nameStr}
  response = requests.post(base_url, json=data)
  if response.status_code == 201:
    return response.json()
  else:
    print('Failed to add collection.')
    return None
  
def add_book(collection_id=None, title=None, genre=None, author=None):
  if (collection_id is None or title is None or genre is None or author is None):
    print('Please specify the collection, title, genre, and author of your book')
    return None
  
  base_url = 'http://localhost:5000/add_book'
  
  titleStr = ''
  for t in title:
    titleStr += t
    titleStr += ' '
  titleStr = titleStr.rstrip()
  
  genreStr = ''
  for g in genre:
    genreStr += g
    genreStr += ' '
  genreStr = genreStr.rstrip()
  
  authorStr = ''
  for a in author:
    authorStr += a
    authorStr += ' '
  authorStr = authorStr.rstrip()
  
  data = {
    'collection_id': collection_id,
    'title': titleStr,
    'genre': genreStr,
    'author': authorStr
  }
  
  response = requests.post(base_url, json=data)
  if response.status_code == 201:
    return response.json()
  else:
    print('Failed to add book.')
    return None

# Function to parse command-line arguments and call the appropriate function
def main():
    parser = argparse.ArgumentParser(description='Book Management CLI')
    parser.add_argument('command', choices=['list_books', 'list_collections', 'add_collection', 'add_book'], help='Command to execute')
    parser.add_argument('--collection_id', help='List all books in the collection or add a book to this collection')
    parser.add_argument('--genre', nargs='+', help='Filter by genre or add a book of this genre')
    parser.add_argument('--author', nargs='+', help='Filter by author or add a book by this author')
    parser.add_argument('--name', nargs='+', help='Add this collection by this name')
    parser.add_argument('--title', nargs='+', help = 'Add a book of this title')
    
    while True:
      # Get user input
      user_input = input('Enter a command: ')

      # Parse user input
      args = parser.parse_args(user_input.split())

      if args.command == 'list_books':
        books = get_books(collection_id=args.collection_id, genre=args.genre, author=args.author)
        if books:
          print('List of books:')
          for book in books:
            print(f"Title: {book[1]}, Genre: {book[2]}, Author: {book[3]}, Collection Id: {book[4]}")
        else:
          print('Invalid command.')
      
      if args.command == 'list_collections':
        collections = get_collections()
        if collections:
          print('List of collections')
          for collection in collections:
            print(f"Id: {collection[0]}, Name: {collection[1]}")
        else:
          print('Invalid command.')
          
      if args.command == 'add_collection':
        response = add_collection(name=args.name)
        if response:
          print(response)
        else:
          print('Invalid command')
      
      if args.command == 'add_book':
        response = add_book(collection_id= args.collection_id, title=args.title, genre=args.genre, author=args.author)
        if response:
          print(response)
        else:
          print('Invalid command')
      

if __name__ == '__main__':
  main()
    
#     # Add a new book
#     add_book('To Kill a Mockingbird', 'Harper Lee', '978-0061120084')
