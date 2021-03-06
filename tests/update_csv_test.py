
import os
from app import db,auth
from app.db.models import User, Song
from app.auth.forms import csv_upload
from flask_login import FlaskLoginClient

def test_upload_csv(application):
    application.test_client_class = FlaskLoginClient
    user = User('ttd22@njit.edu', 'testtest', True)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'ttd22@njit.edu'
    assert db.session.query(User).count() == 1

    root = os.path.dirname(os.path.abspath(__file__))
    music_csv = os.path.join(root, '../uploads/music.csv')

    with application.test_client(user = user) as client:
        # This request already has a user logged in.
        response = client.get('/songs/upload')
        assert response.status_code == 200
        form = csv_upload()
        form.file = music_csv
        assert form.validate


# def test_update_csv_verification(test_client):
#     root = os.path.dirname(os.path.abspath(__file__))
#     music_csv = os.path.join(root, '../uploads/music.csv')
#     response = test_client.post('/songs/upload', data=music_csv)
#     assert response.status_code == 201

def test_upload_csv_denied(application,client):
    application.test_client_class = FlaskLoginClient
    assert db.session.query(User).count() == 0
    with application.test_client(user = None) as client:
        # This request already has a user logged in.
        response = client.get('/songs/upload')
        assert response.status_code == 302