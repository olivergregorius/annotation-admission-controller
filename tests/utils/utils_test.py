from app.utils.utils import get_base64_str


def test_given_a_string_when_get_base64_str_is_called_then_base64_string_is_returned():
    input = 'This is a test string'
    result = get_base64_str(input)
    assert result == 'VGhpcyBpcyBhIHRlc3Qgc3RyaW5n'
