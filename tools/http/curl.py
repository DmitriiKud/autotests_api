from httpx import Request, RequestNotRead


def make_curl_from_request(request: Request) -> str:
    """Generate a cURL command from an HTTPX request.

    The command includes the request method, URL, headers, and body when
    available.

    Args:
        request: HTTPX request to convert.

    Returns:
        A cURL command string.
    """
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    try:
        if body := request.content:
            result.append(f"-d '{body.decode('utf-8')}'")
    except RequestNotRead:
        pass

    return " \\\n  ".join(result)
