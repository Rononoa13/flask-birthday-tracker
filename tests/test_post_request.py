from app import app
# Test post request handling:

def test_add_birthday():
    client = app.test_client()
    data = {'name': 'David', 'month': "12", 'day': '28'}

    response = client.post('/', data=data)

    assert response.status_code == 302

