from flask_jwt_extended import decode_token

def decode_token(token):
    try:
        return decode_token(token).get('identity')
    except Exception as e:
        return None
