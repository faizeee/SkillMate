def test_get_skills(client):
    res = client.get("/api/skills/")
    print("RESPONSE TEXT:", res.text)  # print raw error message
    assert res.status_code == 200
    assert isinstance(res.json(),list)