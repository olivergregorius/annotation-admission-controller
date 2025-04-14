# annotation-admission-controller

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/olivergregorius/annotation-admission-controller/test.yml?branch=main&label=Python%20Test&logo=github)](https://github.com/olivergregorius/annotation-admission-controller/actions/workflows/test.yml)
[![GitHub](https://img.shields.io/github/license/olivergregorius/annotation-admission-controller?label=License)](https://github.com/olivergregorius/annotation-admission-controller/blob/HEAD/LICENSE)

A [Kubernetes Admission Controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) for adding annotations to a Kubernetes
resource.

## Installation

annotation-admission-controller is provided as a [Helm Chart](https://helm.sh/) and can be installed that way.

```shell
helm repo add olivergregorius https://olivergregorius.github.io/helm-charts
helm repo update
helm install annotation-admission-controller olivergregorius/annotation-admission-controller
```

## Configuration

Configuration is done by adjusting the `values.yaml` of the Helm chart. Usually, leaving the default values should be sufficient, but the `annotate` section
should be adjusted to your needs:

```yaml
annotate:
  target:
    apiGroups: [""]
    apiVersions: ["v1"]
    resources: ["persistentvolumeclaims"]
    scope: Namespaced
  operations: ["CREATE", "UPDATE"]
  annotations:
    argocd.argoproj.io/sync-options: Delete=false
```

In the above example, which represents the default settings, each newly created or updated PersistentVolumeClaim is annotated with
`argocd.argoproj.io/sync-options: Delete=false` to indicate that this resource should not be deleted by Argo CD when the respective application is deleted.

Please check the [Kubernetes API Reference](https://kubernetes.io/docs/reference/kubernetes-api/) for a list of all Kubernetes resources.
