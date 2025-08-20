# import os
# from typing import Optional
# from core.config import config
# from fastapi import UploadFile


# def save_file(file:UploadFile, subdir:Optional[str] = None) -> str :
#     """Save Uploaded file and return the file path."""

#     path_to_upload = os.path.join(config.upload_dir,subdir) if subdir else config.upload_dir
