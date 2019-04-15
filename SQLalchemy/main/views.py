from datetime import date
import sqlalchemy.orm
from django.utils.timezone import now
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from sqlalchemy import create_engine
from .serializers import *
from passlib.hash import bcrypt
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import jwt,json


# Create your views here.


engine = create_engine("mysql+pymysql://root:16001700@localhost/test")
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

def createProfile(data,id):
    profile = UserProfile()
    profile.users =id
    profile.updated = date.today()
    profile.created = date.today()
    profile.license_number = data['license_number']
    profile.about = data['about']
    profile.weight = data['weight']
    profile.height=data['height']
    try:
      session.add(profile)
      session.new
      session.commit()

    except:
        session.rollback()
        raise

    finally:
        session.close()

@renderer_classes((JSONRenderer,))
@api_view(['POST'])
def createUser(request):
    profile_data = request.data.get('profile')
    user = User()
    user.email = request.data.get('email')
    user.first_name = request.data.get('first_name')
    user.last_name = request.data.get('last_name')
    user.password = bcrypt.encrypt(request.data.get('password'))
    user.user_type = request.data.get('user_type')
    user.created = date.today()
    user.updated = date.today()
    user.last_login = now()

    try:
        session.add(user)
        session.new
        session.commit()
        profile=createProfile(profile_data, user.id)

    except:
        session.rollback()
        raise

    finally:
        session.close()

    return Response(status=status.HTTP_204_NO_CONTENT)

@renderer_classes((JSONRenderer,))
@api_view(['GET'])

def listUsers(request):
    result =[]
    users = session.query(User).all()
    user_schema = UserSchema()
    profile_schema = UserProfileSchema()
    for user in users :
        result.append(user_schema.dump(user).data)
    return Response(result, status=status.HTTP_200_OK)

@api_view(['PUT'])
def updateUser(request,pk):
    user = session.query(User).filter_by(id = pk).one()
    update_schema = UserUpdateSchema(request.data)
    data = update_schema.dumps(user)
    return Response(data,status.HTTP_200_OK)

@api_view(['POST'])
def login (request):
    password = request.data.get('password')
    email = request.data.get('email')
    user = session.query(User).filter_by(email=email).one()
    if (user.email == email ):

        if bcrypt.verify(password, user.password):
            user.last_login = now()
            payload = {
                'id': user.id,
                'email': user.email,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
            token_schema = TokenSchema()
            token = token_schema.dump(jwt_token).data
            return Response(token, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_418_WRONG_CREDENTIALS)
