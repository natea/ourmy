from django.http import HttpResponseRedirect
from singly import SinglyHelper
from django.contrib.auth import authenticate, login as auth_login
from models import SinglyProfile
from django.contrib.auth.models import User


def authenticate_redirect(request, service):
    url = SinglyHelper.get_authorize_url(service)
    return HttpResponseRedirect(url)


def authorize_callback(request):
    code = request.GET.get('code')
    content = SinglyHelper.get_access_token(code)
    user_profile = SinglyProfile.objects.get_or_create_user(
            content['account'], content['access_token'])
    if not request.user.is_authenticated():
        # ideally, we would be using a randomized password.  Not sure why this isn't working
        # password = User.objects.make_random_password()
        # print "password: " + password
        # user = authenticate(username=user_profile.user.username, password=password)
        user = authenticate(username=user_profile.user.username, password='fakepassword')
        auth_login(request, user)

    # we want to redirect the user back to the campaign they were on before.
    DEFAULT_URL = 'http://www.zoomtilt.com/'
    destination = request.META.get('HTTP_REFERER', DEFAULT_URL)
    MY_BASE_URL = 'http://www.zoomtilt.com/' # trailing slash important
    LOCALLY = "http://localhost:"
    if destination.startswith(MY_BASE_URL) or destination.startswith(LOCALLY):
        return HttpResponseRedirect(destination)
    else:
        return HttpResponseRedirect('/')