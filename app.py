from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# SQLite database file path
DATABASE = 'bms.db'

def connect_db():
  return sqlite3.connect(DATABASE)

@app.route('/collections', methods=['GET'])
def get_collections():
  conn = connect_db()
  cur = conn.cursor()
  cur.execute("SELECT * FROM collections")
  collections = cur.fetchall()
  conn.close()
  if collections:
    return jsonify(collections), 200
  else:
    return jsonify({'message': "No books found"}), 404
  

@app.route('/books', methods=['GET'])
def get_books():
  # Extract query parameters from the URL
  collection_id = request.args.get('collection_id')
  author = request.args.get('author')
  genre = request.args.get('genre')
  
  conn = connect_db()
  cur = conn.cursor()
  
  query = 'SELECT * FROM books'
  if (collection_id and genre and author):
    query += ' WHERE collection_id = ' + collection_id + ' AND genre = \"' + genre + '\" AND author = \"' +author + '\"'
  elif (collection_id and genre):
    query += ' WHERE collection_id = ' + collection_id + ' AND genre = \"' + genre + '\"'
  elif (collection_id and author):
    query += ' WHERE collection_id = ' + collection_id + ' AND author = \"' +author + '\"'
  elif (genre and author):
    query += ' WHERE genre = \"' + genre + '\" AND author = \"' +author + '\"'
  elif (collection_id):
    query += ' WHERE collection_id = ' + collection_id
  elif (genre):
    query += ' WHERE genre = \"' + genre + '\" AND author = \"' +author + '\"'
  elif (author):
    query += ' WHERE author = \"' + author + '\"'
  
  cur.execute(query)
  
  books = cur.fetchall()
  conn.close()
  
  if books:
    return jsonify(books), 200
  else:
    return jsonify({'message': "No books found"}), 404

@app.route('/add_collection', methods=['POST'])
def add_collection():
  data = request.json
  name = data.get('name')
  conn = connect_db()
  cur = conn.cursor()

  query = 'INSERT INTO collections (name) VALUES (\"' + name + '\")'
  cur.execute(query)
  conn.commit()
  conn.close()
  return jsonify({'message': 'Successfully added ' + name}), 201

@app.route('/add_book', methods=['POST'])
def add_book():
  data = request.json
  collection_id = data.get('collection_id')
  title = data.get('title')
  genre = data.get('genre')
  author = data.get('author')
  
  conn = connect_db()
  cur = conn.cursor()

  query = 'INSERT INTO books (title, genre, author, collection_id) VALUES (\"' + title + '\", \"'+ genre +'\", \"' + author + '\", ' + collection_id + ')'
  print(query)
  cur.execute(query)
  conn.commit()
  conn.close()
  return jsonify({'message': 'Successfully added ' + title}), 201

if __name__ == '__main__':
    app.run(debug=True)
