from lib.album import Album

def test_get_albums(db_connection, web_client):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, Title 1, 1998, 3), Album(2, Title 2, 2007, 4), Album(3, Another title, 2023, 1), Album(4, Final title, 1956, 3)"

def test_post_album(db_connection, web_client):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.post('/albums', data = {'title': 'Voyage', 'release_year': 2022, 'artist_id': 2})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album successfully created."
    response_2 = web_client.get('/albums')
    assert response_2.status_code == 200
    assert response_2.data.decode('utf-8') == "Album(1, Title 1, 1998, 3), Album(2, Title 2, 2007, 4), Album(3, Another title, 2023, 1), Album(4, Final title, 1956, 3), Album(5, Voyage, 2022, 2)"

def test_post_album_no_params(db_connection, web_client):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.post('/albums', data = {})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Please enter a title, release year and artist id"
    