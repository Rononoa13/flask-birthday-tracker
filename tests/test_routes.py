from app import app

def test_home_route_returns_200():
    response = app.test_client().get("/")
    assert response.status_code == 200


def test_home_route_contains_birthday_related_content():
    response = app.test_client().get("/")
    content = response.data.decode("utf-8")
    
    assert f"Birthdays" in content
    assert f"Add a Birthday" in content
    assert f"Add Birthday" in content
    assert f"All Birthdays" in content

