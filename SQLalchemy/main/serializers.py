from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from .models import User,UserProfile,UserEducation



class UserProfileSchema(ModelSchema):
    class Meta :
        model = UserProfile

class UserSchema(ModelSchema):
    profile = fields.Nested(UserProfileSchema())
    class Meta :
        model = User

