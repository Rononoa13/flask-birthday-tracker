from app import app

def test1():
    response = app.test_client().get("/")
    assert response.status_code == 200

def test2():
    response = app.test_client().get("/")
    assert b"Birthdays" in response.data
    assert b"Add a Birthday" in response.data
    assert b"Add Birthday" in response.data
    assert b"All Birthdays" in response.data
    # assert b"Delete" in response.data
