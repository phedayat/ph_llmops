import os

from enum import Enum
from base64 import b64encode
from typing import Union, Optional


class ImageDetails(str, Enum):
    AUTO: str = "auto"
    LOW: str = "low"
    HIGH: str = "high"


def system(message: str) -> dict[str, str]:
    return {"role": "system", "content": message}


def user(
    message: Union[str, dict]
) -> Optional[dict[str, Union[str, list[dict[str, Union[str, dict]]]]]]:
    if not message: return None
    if isinstance(message, str):
        content = {"type": "text", "text": message}
    else:
        content = message
    return {"role": "user", "content": [content]}


def _encode_image(image_path: str) -> str:
    with open(image_path, "rb") as f:
        return b64encode(f.read()).decode()


def image(
    image_path: str, 
    detail: str = ImageDetails.AUTO.value,
) -> dict[str, Union[str, dict[str, str]]]:
    if detail not in ImageDetails:
            return None

    if not image_path.startswith("https"):
        image_enc = _encode_image(image_path)
        ext = os.path.splitext(image_path)[1][1:]
        url = f"data:image/{ext};base64,{image_enc}"
    else:
        url = image_path

    
    return {
        "type": "image_url",
        "image_url": {"url": url, "detail": detail}
    }