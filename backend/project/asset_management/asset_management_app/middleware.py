from graphql_jwt.utils import jwt_decode


class VerifyAccessTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Bearer '):
            access_token = auth_header[7:]
            try:
                decoded_payload = jwt_decode(access_token)
                # Attach the decoded payload to the request
                request.access_token_payload = decoded_payload
            except Exception as e:
                # Handle token verification errors here
                pass  # For example, log the error
        return self.get_response(request)
