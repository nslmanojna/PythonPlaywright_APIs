from playwright.sync_api import APIRequestContext

def test_add_book_success(api_context: APIRequestContext, add_book):
    #Get Endpoint and Payload from add_book fixture
    endpoint = add_book["endpoint"]
    payload = add_book["payload"]

    # Send POST request
    response = api_context.post(endpoint, data=payload)

    # Assertions
    assert response.status == 200
    response_json = response.json()
    print("Response:", response_json)

    assert response_json["Msg"] == "successfully added"
    assert "ID" in response_json
    assert response_json["ID"].startswith("QE")
