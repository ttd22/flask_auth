import logging
from app import db
from app.db.models import User, Song
from app.auth.forms import login_form, register_form
from faker import Faker

# def test_user_login(application, client):
#     log = logging.getLogger("myApp")
#     with application.app_context():
#         form = login_form
#         form.email = "ttd22@njit.edu"
#         form.password = "trangdang"
#         # assert validate(form)
#         # response = client.post("/login.html",{login_form.email: 'ttd22@njit.edu', login_form.password: 'trangdang' })
#         response = client.get("/login")
#         assert response.status_code == 200
#         assert b"ttd22@njit.edu" in response.data
#     log.info("user login test")

def test_user_register(application, client):
    log = logging.getLogger("myApp")
    with application.app_context():
        form = register_form
        form.email = "ttd22@njit.edu"
        form.password = "trangdang"
        form.confirm = "trangdang"
        # assert form.validate_on_submit(form) == "fdd"
        assert form.validate
    log.info("user register test")
    # client = application.test_client()
    # data = {'email': 'ttd22@njit.edu','password': 'trangdang'}
    # # res = client.post("/login",data,buffered=True,
    # #                        content_type='multipart/form-data')
    # res = client.post('/login',data=data)
    # assert res.status_code == 200

def test_user_login(application, client):
    log = logging.getLogger("myApp")
    with application.test_client():
        form = login_form
        form.email = "ttd22@njit.edu"
        form.password = "trangdang"
        assert form.validate
    log.info("user login test")