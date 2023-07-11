from typing import Any, Callable, Dict, Iterable, Tuple, Optional

from requests import Response
from requests_html import Element


URL = str
Options = Dict[str, Any]
Post = Dict[str, Any]
Profile = Dict[str, Any]
RequestFunction = Callable[[URL, Optional[Any]], Response]
RawPage = Element
RawPost = Element
Page = Iterable[RawPost]
Credentials = Tuple[str, str]
