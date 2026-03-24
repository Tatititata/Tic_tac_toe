from datasource.model.user_model import UserModel
from domain import User


class UserMapper:

    def to_entity(self, user:User):
        u = user.to_dict()
        return UserModel.from_dict(u)
    
    def to_domain(self, user:UserModel):
        u = user.to_dict()
        return User.from_dict(u)
