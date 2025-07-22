from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "secretkeychangeit" # !! IMPORTANT: Change this in production !! and should NEVER be used in a production environment. this should be a strong, randomly generated secret key, ideally loaded from environment variables or a secure vault.
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 

pwd_context = CryptContext(schemes=['bcrypt'],deprecated="auto")

def verify_password(plain: str, hashed: str) -> bool:
    """Verifies a plain password against a hashed password."""
    return pwd_context.verify(plain, hashed)

def get_password_hash(password: str) -> str:
    """Hashes a plain password."""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: int | None = None) -> str:
    """Creates a JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (timedelta(minutes=expires_delta if(expires_delta) else ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
