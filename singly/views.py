from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from singly import SinglyHelper
from django.contrib.auth import authenticate, login as auth_login
from models import SinglyProfile


def authenticate_redirect(request, service):
    url = SinglyHelper.get_authorize_url(service)
    return HttpResponseRedirect(url)


def authorize_callback(request):
    code = request.GET.get('code')
    content = SinglyHelper.get_access_token(code)
    user_profile = SinglyProfile.objects.get_or_create_user(
            content['account'], content['access_token'])
    if not request.user.is_authenticated():
        user = authenticate(username=user_profile.user.username, password='fakepassword')
        password = User.objects.make_random_password()
        user.set_password(password)
        auth_login(request, user)

    DEFAULT_URL = 'http://example.com/wherever/'
    destination = request.META.get('HTTP_REFERER', DEFAULT_URL)
    MY_BASE_URL = 'http://zoomtilt.com/' # trailing slash important
    LOCALLY = "http://localhost:"
    if destination.startswith(MY_BASE_URL) or destination.startswith(LOCALLY):
        return HttpResponseRedirect(destination)
    else:
        return HttpResponseRedirect('/')