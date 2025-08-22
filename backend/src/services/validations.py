from fastapi import File, HTTPException, UploadFile


def validate_image(
    file: UploadFile | None = File(None),
    max_size_mb: int = 5,
    allowed_types: list[str] = ["image/"],
) -> UploadFile | None:
    """Validate image file."""
    if not file:
        return None

    if not any(file.content_type.startswith(t) for t in allowed_types):
        raise HTTPException(
            status_code=400, detail=f"Invalid file type: {file.content_type}"
        )

    contents = file.file.read()
    if len(contents) > (max_size_mb * 1024 * 1024):
        raise HTTPException(status_code=400, detail="File too large")

    file.file.seek(0)

    return file
