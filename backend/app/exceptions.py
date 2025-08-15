# app/exceptions.py
class IntegrityException(Exception):
    """Raised when there's a data integrity issue (e.g., duplicate email/username)"""
    pass

class DuplicateException(Exception):
    """Raised when an attempt is made to create a duplicate entry"""
    pass

class  AuthenticationException(Exception):
    """Raised when authentication fails (e.g., invalid email/password)"""
    pass

class NotFoundException(Exception):
    """Raised when a requested resource is not found"""
    pass