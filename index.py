import pulumi
import pulumi_kubernetes as k8s

# Configuração do provedor do Kubernetes (local)
k8s_provider = k8s.Provider(
    "k8s-provider",
    kubeconfig="/path/to/your/kubeconfig.yaml",  # Substitua pelo caminho correto
)

# Defina um Deployment e um Service de exemplo
app_labels = {"app": "example"}
deployment = k8s.apps.v1.Deployment(
    "example-app",
    metadata={"labels": app_labels},
    spec={
        "replicas": 2,
        "selector": {"match_labels": app_labels},
        "template": {
            "metadata": {"labels": app_labels},
            "spec": {
                "containers": [{
                    "name": "example-app",
                    "image": "nginx:1.16",
                }],
            },
        },
    },
    opts=pulumi.ResourceOptions(provider=k8s_provider),
)

service = k8s.core.v1.Service(
    "example-service",
    metadata={"labels": app_labels},
    spec={
        "selector": app_labels,
        "ports": [{"port": 80, "target_port": 80}],
    },
    opts=pulumi.ResourceOptions(provider=k8s_provider),
)
