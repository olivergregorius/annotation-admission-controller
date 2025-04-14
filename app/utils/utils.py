import base64


def get_base64_str(input: str) -> str:
    return base64.b64encode(input.encode()).decode()
