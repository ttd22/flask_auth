import logging
import os

from werkzeug.datastructures import FileStorage

from app import db,auth
from app.db.models import User, Song
from io import BytesIO
from app.auth.forms import *
from flask import Blueprint, render_template, abort, url_for, current_app


def test_csv_verification(application):
    with application.app_context():
        root = os.path.dirname(os.path.abspath(__file__))
        music_csv = os.path.join(root, '../uploads/music.csv')
        # assert os.path.exists(music_csv)
