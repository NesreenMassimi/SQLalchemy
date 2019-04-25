'''from main.models import *
from rest_framework import permissions
from main.models import user
import sqlalchemy.orm



engine = create_engine("mysql+pymysql://root:16001700@localhost/test")
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        obj = session.query(User).filter_by(id=view.kwargs['pk'])
        #return obj.id == request.user.id

    def has_object_permission(self, request, view, obj):
        print("in has object permission")
        """
        Return True if permission is granted, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS: # SAFE_METHODS = GET,HEAD,OPTIONS
            return True

        # Write permissions are only allowed to the owner of the snippet.
        else :
            return request.user and request.user.is_authenticated





'''
'''

class ObjectPermissionsBackend(object ):
    
    def has_perm( self,user_obj,perm, obj=None):
        if not obj:
            print("not obj")
            return False # not dealing with non-object permissions

        if perm == 'view':
            return True # anyone can view
        elif obj.author_id == user_obj.id:
            return True
        else:
            print("not auth")
            return False'''