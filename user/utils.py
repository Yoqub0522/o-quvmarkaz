from django.shortcuts import redirect

from user.models import Role


def checking_user(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return func(request,*args,**kwargs)
    return wrapper

def checking_role(func):
    def wrapper(request,*args,**kwargs):
        if  request.user.is_authenticated:
            if request.user.role==Role.ADMIN:
               return func(request,*args,**kwargs)
            else:
                raise PermissionError

        else:
            raise PermissionError
    return wrapper
