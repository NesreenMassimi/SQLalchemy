
from marshmallow_sqlalchemy import ModelSchema
from .models import User



'''class UserProfileSchema(Schema):
    class Meta :
        fields=()'''
class UserSchema(ModelSchema):
    class Meta :
        model = User
