from flask.testing import FlaskClient

from src.models import Movie,db
from tests.utils import refresh_db,create_movie
def test_get_all_movies(test_app:FlaskClient):
        refresh_db()
        test_movie = create_movie()

        res = test_app.get('/movies')
        page_data: str = res.data.decode()
        assert res.status_code == 200
        assert  f'<td><a href="/movies/{ test_movie.movie_id}">The Dark Knight</a></td>' in page_data
        assert '<td>Christopher Nolan1</td>' in page_data
        assert '<td>5</td>' in page_data

def test_get_all_movies_emplty(test_app:FlaskClient):
    refresh_db()
    db.session.commit()
    res = test_app.get('/movies')
    page_data: str = res.data.decode()

    assert res.status_code == 200
    assert '<td>' not in page_data

def test_get_single_movie(test_app:FlaskClient):
    refresh_db()
    test_movie = create_movie(rating=4)

    res = test_app.get(f'/movies/{test_movie.movie_id}')
    page_data: str = res.data.decode()

    assert'<h1>The Dark Knight - 4</h1>' in page_data
    assert'<h2>Christopher Nolan</h2>' in page_data