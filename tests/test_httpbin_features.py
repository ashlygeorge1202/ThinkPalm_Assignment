def test_post_request_with_faker(client, faker):
    # Generate random user with faker
    user = {
        "name": faker.name(),
        "email": faker.email(),
        "address": faker.address()
    }

    # Send POST request
    response = client.post("/post", json=user)

    # Validate response
    assert response.status_code == 200
    json_data = response.json()

    # httpbin echoes back the JSON we send
    assert json_data["json"] == user


def test_status_codes(client):
    # Check a successful status
    response_ok = client.status(200)
    assert response_ok.status_code == 200

    # Check a not found status
    response_not_found = client.status(404)
    assert response_not_found.status_code == 404
