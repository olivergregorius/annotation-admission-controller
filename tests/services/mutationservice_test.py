from app.services.mutationservice import MutationService
from tests.services.mutationservice_fixtures import object_without_annotations, object_with_annotations, annotations_to_add, patch_adding_annotations, \
    patch_replacing_annotations

mutationService = MutationService()


def test_given_object_without_annotations_when_annotate_is_called_then_annotations_are_added(object_without_annotations, annotations_to_add,
                                                                                             patch_adding_annotations):
    result = mutationService.annotate(object_without_annotations, annotations_to_add)
    assert result == patch_adding_annotations


def test_given_object_with_annotations_when_annotate_is_called_then_annotations_are_replaced(object_with_annotations, annotations_to_add,
                                                                                             patch_replacing_annotations):
    result = mutationService.annotate(object_with_annotations, annotations_to_add)
    assert result == patch_replacing_annotations
