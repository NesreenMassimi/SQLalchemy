from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from .models import user,UserProfile,UserEducation


class TokenSchema(ModelSchema):
    class Meta :
        model = user
        fields=('token',)

class UserProfileSchema(ModelSchema):
    class Meta :
        model = UserProfile


class UserSchema(ModelSchema):
    profile = fields.Nested(UserProfileSchema())
    class Meta :
        model = user

class UserUpdateSchema(ModelSchema):

    class Meta :
        model = user
        exclude = ("id", "created")

