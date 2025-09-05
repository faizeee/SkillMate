import errno
import pytest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch
from utils.helpers import save_file
from tests.utils.helpers import fake_upload_file

# @pytest.mark.asyncio
# async def test_save_file_unit(mocker: MockerFixture,tmp_path:Path) :
#     """Unit test for save_file utility."""
#     mock_makedirs = mocker.patch("os.makedirs")
#     test_file = tmp_path/"test.png"
#     test_file.write_bytes(b"fake image data")
#     upload_file = UploadFile(
#         filename="test.png",
#         file=open(test_file,"rb")
#     )

#     print(upload_file)
#     saved_path = await save_file(upload_file, "testdir")

#     mock_makedirs.assert_called_once_with(
#         os.path.join(config.upload_dir, "testdir"), exist_ok=True
#     )
#     assert saved_path.endswith(".png")
#     assert os.path.exists(saved_path)


@pytest.mark.asyncio
async def test_save_file_unit(tmp_path: Path):
    """Unit test save file utility."""
    upload_file = fake_upload_file(tmp_path, file_ext=".png")
    sub_dir = "skills"
    expected_save_path = tmp_path / sub_dir

    saved_path = await save_file(upload_file, subdir=sub_dir, base_dir=str(tmp_path))
    saved_file_url = Path(saved_path)

    assert saved_file_url.suffix == ".png"
    assert saved_file_url.parent == expected_save_path
    assert saved_file_url.exists()

    # assert saved_path.endswith(".png")
    # assert expected_save_path.exists()
    # assert expected_save_path.joinpath(saved_path.split(os.sep)[-1]).exists()


@pytest.mark.parametrize(
    "error_type,error_message",
    [
        (errno.ENOSPC, "No space left on device"),
        (errno.EIO, "I/O error"),
    ],
    ids=["os-error-no-space-left-on-device", "os_error-io-error"],
)
@pytest.mark.asyncio
async def test_save_file_unexpected_os_errors(
    tmp_path: Path, error_type: errno, error_message: str
):
    """Test expected os error related to io operations."""
    upload_file = fake_upload_file(tmp_path)
    with patch("utils.helpers.aiofiles.open", new_callable=MagicMock()) as mock_open:
        mock_file = AsyncMock()
        mock_open.return_value.__aenter__.return_value = mock_file
        mock_file.write.side_effect = OSError(error_type, error_message)

        with pytest.raises(OSError) as exc_info:
            await save_file(upload_file, subdir="skills", base_dir=str(tmp_path))

        assert exc_info.value.errno == error_type


@pytest.mark.asyncio
async def test_save_file_permission_error(tmp_path: Path):
    """Test save file permissions error."""
    upload_file = fake_upload_file(tmp_path)
    with patch("utils.helpers.aiofiles.open", new_callable=MagicMock()) as mock_open:
        mock_file = AsyncMock()
        mock_open.return_value.__aenter__.return_value = mock_file
        mock_file.write.side_effect = PermissionError("Permission denied")

        with pytest.raises(PermissionError):
            await save_file(upload_file, subdir="skills", base_dir=str(tmp_path))
