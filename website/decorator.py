from functools import wraps
from landing.models import Sector


def set_sectors_with_governance(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        request.sectors = Sector.objects.all()
        return view_func(request, *args, **kwargs)

    return wrapper
