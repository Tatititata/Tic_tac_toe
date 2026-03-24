
from domain import User


class UserMapper:

    def to_repo(self, user:User):
        return user.to_dict()
    
    def from_repo_to_user(self, row):
        user = {
                'uid': row.uid,
                'login': row.login,
                'password_hash': row.password_hash
                }
        return User.from_dict(user)
