from django.shortcuts import redirect
from functools import wraps

def role_required(allowed_roles=[]):
    """
    Decorador para verificar si el usuario tiene un rol permitido.
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.role in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('users:no_permitido')  # Redirigir si no tiene permiso
            else:
                return redirect('users:login')  # Redirigir al login si no está autenticado
        return wrapper_func
    return decorator
