import os

from fastapi.testclient import TestClient

from tests.routes.mutations_fixtures import admission_review_without_annotations_request, \
    admission_review_successful_response

os.environ["ANNOTATIONS"] = "annotation1:value1"

from app.main import app

client = TestClient(app)


def test_given_valid_request_when_post_annotate_is_called_then_request_is_successful(admission_review_without_annotations_request,
                                                                                     admission_review_successful_response):
    response = client.post(
        url='/annotate',
        headers={'Content-Type': 'application/json'},
        json=admission_review_without_annotations_request
    )
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json() == admission_review_successful_response
