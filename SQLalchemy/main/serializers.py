from marshmallow import Schema, fields


'''class UserProfileSchema(Schema):
    class Meta :
        fields=()'''

class UserSchema(Schema):
    class Meta :
        fields=("id","first_name","last_name","email","password","user_type","created","updated","last_login")
