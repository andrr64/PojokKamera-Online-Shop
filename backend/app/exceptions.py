# app/exceptions.py
class IntegrityException(Exception):
    """Raised when there's a data integrity issue (e.g., duplicate email/username)"""
    pass