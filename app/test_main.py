from unittest.mock import patch
import pytest

from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
    mock_valid_url: object,
    mock_has_internet: object,
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_not_accessible(
    mock_valid_url: object,
    mock_has_internet: object,
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    result = can_access_google_page("invalid-url")
    assert result == "Not accessible"
