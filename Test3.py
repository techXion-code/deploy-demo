def get_user(id):
    user = db.users.find(id)
    return user
