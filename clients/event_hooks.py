import allure
from httpx import Request

from tools.http.curl import make_curl_from_request


def curl_event_hook(request: Request) -> None:
    """Attach the request as a cURL command to the Allure report."""
    curl_command = make_curl_from_request(request)
    allure.attach(
        curl_command,
        name="cURL command",
        attachment_type=allure.attachment_type.TEXT,
    )
