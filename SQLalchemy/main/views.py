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
from rest_framework import viewsets
from main.models import user

# Create your views here.

engine = create_engine("mysql+pymysql://root:16001700@localhost/test")
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()


@api_view(['POST'])
def log_in (request):
    password = request.data.get('password')
    email = request.data.get('email')
    account = session.query(user).filter_by(email=email).one()
    if account.email == email :
        if bcrypt.verify(password, account.password):
            request.session['user_id'] = account.id
            account.last_login = now()
            return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_418_WRONG_CREDENTIALS)


@api_view(['GET'])
def log_out (request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return Response(status.HTTP_200_OK)




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
    account = user()
    account.email = request.data.get('email')
    account.first_name = request.data.get('first_name')
    account.last_name = request.data.get('last_name')
    account.password = bcrypt.encrypt(request.data.get('password'))
    account.user_type = request.data.get('user_type')
    account.created = date.today()
    account.updated = date.today()
    account.last_login = now()

    try:
        session.add(account)
        session.new
        session.commit()
        profile=createProfile(profile_data, account.id)

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
    accounts = session.query(user).all()
    user_schema = UserSchema()
    profile_schema = UserProfileSchema()
    for us in accounts:
        result.append(user_schema.dump(us).data)
    return Response(result, status=status.HTTP_200_OK)

def is_logedin(request):
    if 'user_id' in request.session:
            return True
    return False

class Updateview(viewsets.ModelViewSet) :


    def update_user(self,user, data):

        if data.get('first_name') is not None:
            user.first_name = data.get('first_name')

        if data.get('last_name') is not None:
            user.last_name = data.get('last_name')

        if data.get('user_type') is not None:
            user.user_type = data.get('user_type')

        if data.get('email') is not None:
            user.email = data.get('email')

        if data.get('password') is not None:
            user.password = bcrypt(data.get('password'))
        user.updated = date.today()

    def update(self, request,*args, **kwargs):
            account = session.query(user).filter_by(id=kwargs['pk']).one()
            created = account.created
            if account is not None:
                if is_logedin(request):
                    print(request.session['user_id'])
                    data = request.data
                    if(request.session['user_id']== account.id):
                      self.update_user(account, data)
                      account.created = created
                      account.id = kwargs['pk']
                      user_schema = UserSchema()
                      result = user_schema.dump(account).data
                      session.add(account)
                      session.commit()
                      return Response(result, status.HTTP_200_OK)
                    return Response(status.HTTP_401_UNAUTHORIZED)

                return Response("details : Login Required ")

            return Response(status.HTTP_404_NOT_FOUND)

