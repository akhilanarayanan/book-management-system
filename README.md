# book-management-system
This is a simple book management system that provides a REST API, stores its data in a relational database, and has a CLI client that can interact with it.

## How to run
In one terminal, run ```python app.py```

In a separate terminal, run ```python client.py```

The client will prompt you to enter a command. Type one of the valid CLI commands and hit enter.

## CLI commands
My CLI commands will expose REST APIs for managing the books. Users can issue direct http calls via curl, or they can use my CLI commands. I will list the CLI commands and explain what they allow users to do.

•	```list_books``` 

This will just list all the books put into the server from various collections and include title, author, and genre. 

This will also take 3 optional filters: ```--collection_id```, ```--genre```, and ```--author```. For example: ```list_books --collection_id 1 --genre fantasy``` will list all the fantasy books in collection 1. If a user forgets their collection id, but remembers their collection name, they can call ```list_collections``` and find their collection id.

•	```list_collections```

This will list all the collections and their ids

•	```add_collection --name <name>```

This will allow users to create a new collection.

•	```add_book --collection_id `<id>` --title `<title>` --author `<author>` --genre `<genre>````

This will allow users to add books to a collection.

## REST APIs
•	bms list books => GET /books

   o	bms list books --collection_id `<id>` => GET /books?collection_id=`<id>`
   
   o	bms list books --genre `<genre>` => GET /books?genre=`<genre>`

   o	bms list books --author `<author>` => GET /books?author=`<author>`

   o	bms list books --collection_id `<id>` --genre `<genre>` --author `<author>` => GET /books?collection_id=`<id>`&genre=`<genre>`&author=`<author>`
 
•	bms list collections => GET /collections
 
•	bms add collection --name `<name>` => POST /add_collection?name=`<name>`
 
•	bms add book --collection_id `<id>` --title `<title>` --author `<author>` --genre `<genre>` => POST /add_book?collection_id=`<id>`&title=`<title>`&genre=`<genre>`&author=`<author>`

## Database Structure 
The ID column of each table will be the primary key. 

Collections Table:	

ID | Name

1  | Collection 1

2	 | Collection 2

3	 | Collection 3


Books Table: Collection Id is a foreign key referencing Id of Collections Table

Id | Title                     | Genre           | Author             | Collection Id

1	 | The Hobbit	               | Fantasy	        | J. R. R. Tolkien	  | 1

2	 | Gone Girl	        	       | Thriller        | Gillian Flynn	     | 1

3	 | Strangers on a Train	     | Thriller	       | Patricia Highsmith	| 2

4	 | The Left Hand of Darkness | Science Fiction | Ursula K. Le Guin	 | 3



