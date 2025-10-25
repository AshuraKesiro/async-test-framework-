def validate_user_schema(user):
    assert "id" in user
    assert "name" in user
    assert "email" in user
