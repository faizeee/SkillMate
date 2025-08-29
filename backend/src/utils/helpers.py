import os
from typing import Optional
from uuid import uuid4
from core.config import config
from fastapi import UploadFile
import aiofiles


async def save_file(
    file: UploadFile, subdir: Optional[str] = None, base_dir: Optional[str] = None
) -> str:
    """Save Uploaded file and return the file path."""
    # creates upload path string
    upload_dir = base_dir or config.upload_dir
    base_path = os.path.join(upload_dir, subdir) if subdir else upload_dir
    # make directory exist_ok=True is a crucial argument.
    os.makedirs(base_path, exist_ok=True)
    _, file_ext = os.path.splitext(file.filename)
    file_name = f"{uuid4().hex}{file_ext}"
    path = os.path.join(base_path, file_name)
    async with aiofiles.open(path, "wb") as out_file:
        while content := await file.read(1024 * 1024):  # 1 MB
            await out_file.write(content)

    return path


def asset(path: Optional[str]) -> str:
    """Generate a full URL for static assets.

    Example:
        asset("icons/logo.png") -> http://localhost:8000/static/icons/logo.png
    """
    base_url = config.app_url.rstrip("/")
    if path:
        return f"{base_url}/static/{path.lstrip('/')}"
    return base_url
