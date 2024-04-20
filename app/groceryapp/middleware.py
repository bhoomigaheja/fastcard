from django.contrib.auth import authenticate, login

class LoginAsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if not request.user.is_authenticated:
            if 'login_as' in request.session:
                user = authenticate(request, pk=request.session['login_as'])
                if user:
                    # Save original admin user ID and current user ID
                    request.session['original_user_id'] = request.user.pk
                    request.session['current_user_id'] = user.pk
                    login(request, user)
                    request.user = user
            elif 'original_user_id' in request.session:
                original_user_id = request.session.pop('original_user_id')
                user = authenticate(request, pk=original_user_id)
                if user:
                    login(request, user)
                    # Restore current user ID
                    request.user.id = request.session.pop('current_user_id')

        return response
