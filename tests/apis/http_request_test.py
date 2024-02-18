import pytest
from unittest.mock import patch
from requests.exceptions import ConnectionError, Timeout
from streaming_converter.apis.http_request import req


@patch("streaming_converter.apis.http_request.time.sleep")
@patch("streaming_converter.apis.http_request.request")
def test_req_exceptions(mock_request, mock_sleep):
    # Makes sleep being instantaneous for faster testing
    mock_sleep.return_value = None

    url = "https://test.test.com"
    retries = 5

    mock_request.side_effect = Timeout()
    with pytest.raises(
        Timeout,
        match=f"Timeout Error on {url} after {retries} attempts",
    ):
        _ = req("GET", url=url, retries=retries)

    mock_request.side_effect = ConnectionError()
    with pytest.raises(
        ConnectionError,
        match=f"Connection Error on {url} after {retries} attempts",
    ):
        _ = req("GET", url=url, retries=retries)


@pytest.mark.parametrize(
    "status_code, message, expected",
    [
        (200, "success", (True, "success")),
        (404, "fail", (False, "fail")),
    ],
)
@patch("streaming_converter.apis.http_request.request")
def test_req(mock_request, status_code, message, expected):
    mock_request.return_value.response = message
    mock_request.return_value.status_code = status_code

    is_ok, r = req("GET", url="https://test.test.com", retries=5)

    assert is_ok == expected[0]
    assert r.response == expected[1]
