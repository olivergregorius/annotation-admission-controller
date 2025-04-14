import pytest

from app.services.mutationservice import Patch


@pytest.fixture
def object_without_annotations():
    return {
        'apiVersion': 'v1',
        'kind': 'PersistentVolumeClaim',
        'metadata': {
            'name': 'test-pvc'
        },
        'spec': {
            'storageClassName': 'default',
            'accessModes': ['ReadWriteOnce'],
            'resources': {
                'requests': {
                    'storage': '1Gi'
                }
            }
        }
    }


@pytest.fixture
def object_with_annotations():
    return {
        'apiVersion': 'v1',
        'kind': 'PersistentVolumeClaim',
        'metadata': {
            'name': 'test-pvc',
            'annotations': {
                'existingAnnotation': 'existingValue'
            }
        },
        'spec': {
            'storageClassName': 'default',
            'accessModes': ['ReadWriteOnce'],
            'resources': {
                'requests': {
                    'storage': '1Gi'
                }
            }
        }
    }


@pytest.fixture
def annotations_to_add():
    return 'newAnnotation1:value1,newAnnotation2:value2'


@pytest.fixture
def patch_adding_annotations():
    return Patch(
        op='add',
        path='/metadata/annotations',
        value={
            'newAnnotation1': 'value1',
            'newAnnotation2': 'value2'
        }
    ).toJson()


@pytest.fixture
def patch_replacing_annotations():
    return Patch(
        op='replace',
        path='/metadata/annotations',
        value={
            'existingAnnotation': 'existingValue',
            'newAnnotation1': 'value1',
            'newAnnotation2': 'value2'
        }
    ).toJson()
