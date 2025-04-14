import pytest


@pytest.fixture
def admission_review_without_annotations_request():
    return {
        'apiVersion': 'admission.k8s.io/v1',
        'kind': 'AdmissionReview',
        'request': {
            'uid': '123456',
            'kind': {
                'group': '',
                'version': 'v1',
                'kind': 'PersistentVolumeClaim'
            },
            'resource': {
                'group': '',
                'version': 'v1',
                'resource': 'persistentvolumeclaims'
            },
            'operation': 'CREATE',
            'object': {
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
        }
    }


@pytest.fixture
def admission_review_successful_response():
    return {
        'apiVersion': 'admission.k8s.io/v1',
        'kind': 'AdmissionReview',
        'response': {
            'uid': '123456',
            'allowed': True,
            'patchType': 'JSONPatch',
            'patch': 'W3sib3AiOiAiYWRkIiwgInBhdGgiOiAiL21ldGFkYXRhL2Fubm90YXRpb25zIiwgInZhbHVlIjogeyJhbm5vdGF0aW9uMSI6ICJ2YWx1ZTEifX1d'
        }
    }
