async def test_main(async_client):
    response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "There are no errors here"}