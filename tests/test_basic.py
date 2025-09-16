def test_get_request(client):
    # Call httpbin GET endpoint
    response = client.get("/get", params={"foo": "bar"})

    # Validate response
    assert response.status_code == 200
    json_data = response.json()

    # httpbin echoes back query params
    assert json_data["args"]["foo"] == "bar

