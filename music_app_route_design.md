
# music_web_app Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
method: POST
path: /albums
body params:  title, release_year, artist_id
returns: None

method: GET
path: /albums
body params: none
returns: all albums

```

## 2. Create Examples as Tests


```python
POST /albums {'title': 'Voyage', 'release_year': 2022, 'artist_id': 2}
response: 200
returns: None

POST /albums {}
reponse 404
returns: "Please enter a title, release year and artist id"

GET /albums
reponse: 200
returns: list of albums

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

def test_get_albums(db_connection, web_client):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, 'Title 1', 1998, 3), Album(2, 'Title 2', 2007, 4), Album(3, 'Another title', 2023, 1), Album(4, 'Final title', 1956, 3)"

def test_post_album(db_connection, web_client):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.post('/albums', data = {'title': 'Voyage', 'release_year': 2022, 'artist_id': 2})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album successfully created."
    response_2 = web_client.get('/albums')
    assert response_2.status_code == 200
    assert response_2.data.decode('utf-8') == "Album(1, 'Title 1', 1998, 3), Album(2, 'Title 2', 2007, 4), Album(3, 'Another title', 2023, 1), Album(4, 'Final title', 1956, 3), Album(5, 'Voyage', 2022, 2)"


def test_post_album_no_params(db_connection, web_client):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.post('/albums', data = {})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Please enter a title, release year and artist id"
```

