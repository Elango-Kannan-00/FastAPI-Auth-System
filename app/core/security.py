import bcrypt

def _ensure_bcrypt_safe_length(password: str) -> str:
    if len(password.encode("utf-8")) > 72:
        raise ValueError("Password must be 72 bytes or fewer when UTF-8 encoded")
    return password

# Hashing input password during signup.
def hash_password(password: str):
    secret = _ensure_bcrypt_safe_length(password).encode("utf-8")
    return bcrypt.hashpw(secret, bcrypt.gensalt()).decode("utf-8")

# Verifying input password during log in.
def verify_password(plain: str, hashed: str):
    secret = _ensure_bcrypt_safe_length(plain).encode("utf-8")
    return bcrypt.checkpw(secret, hashed.encode("utf-8"))

