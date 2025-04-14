import json
import logging

logging.basicConfig(format="[%(asctime)s] %(levelname)s: %(message)s")
mutations = logging.getLogger(__name__)
mutations.setLevel(logging.INFO)


class Patch:
    op: str
    path: str
    value: object

    def __init__(self, op: str, path: str, value: object):
        self.op = op
        self.path = path
        self.value = value

    def toJson(self) -> str:
        return json.dumps([{
            'op': self.op,
            'path': self.path,
            'value': self.value
        }])


class MutationService:
    def annotate(self, object: dict, annotations: str) -> str:
        object_annotations = {}
        patch_type = 'add'
        if 'annotations' in object['metadata']:
            object_annotations = object['metadata']['annotations']
            patch_type = 'replace'

        annotation_list = annotations.replace(' ', '').split(',')
        for annotation in annotation_list:
            mutations.info(f'Applying annotation {annotation} to {object["kind"]}/{object["metadata"]["name"]}.')
            label, value = annotation.replace(' ', '').split(':')
            object_annotations[label] = value

        return Patch(op=patch_type, path='/metadata/annotations', value=object_annotations).toJson()
