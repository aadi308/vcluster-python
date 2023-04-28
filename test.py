import yaml
from kubernetes import client, config


# Load the YAML file into a Python dictionary
with open('cluster.yaml') as f:
    custom_resource = yaml.safe_load(f)

    # Load Kubernetes configuration
    config.load_kube_config()

    # Create a Kubernetes API client instance
    api_instance = client.CustomObjectsApi()

    # Create the custom resource in the cluster
    api_instance.create_namespaced_custom_object(
        group="cluster.x-k8s.io",
        version="v1beta1",
        namespace="ha-vcluster",
        plural="clusters",
        body=custom_resource
    )

    # Load the YAML file into a Python dictionary
with open('vcluster.yaml') as f:
    custom_resource2 = yaml.safe_load(f)

    # Load Kubernetes configuration
    config.load_kube_config()

    # Create a Kubernetes API client instance
    api_instance = client.CustomObjectsApi()

    # Create the custom resource in the cluster
    api_instance.create_namespaced_custom_object(
        group="infrastructure.cluster.x-k8s.io",
        version="v1alpha1",
        namespace="ha-vcluster",
        plural="vclusters",
        body=custom_resource2
    )

# from fastapi import FastAPI
# import yaml
# from kubernetes import client, config

# app = FastAPI()
# config.load_kube_config()

# # Create a Kubernetes API client instance
# custom_object_api = client.CustomObjectsApi()

# @app.post("/create")
# def create():
# # Load the YAML file into a Python dictionary
#     with open('cluster.yaml') as f:
#         custom_resource = yaml.safe_load(f)

#     # Load Kubernetes configuration
#     config.load_kube_config()

#     # Create a Kubernetes API client instance
#     api_instance = client.CustomObjectsApi()

#     # Create the custom resource in the cluster
#     api_instance.create_namespaced_custom_object(
#         group="cluster.x-k8s.io",
#         version="v1beta1",
#         namespace="ha-vcluster",
#         plural="clusters",
#         body=custom_resource
#     )

#     # Load the YAML file into a Python dictionary
#     with open('vcluster.yaml') as f:
#         custom_resource2 = yaml.safe_load(f)

#     # Load Kubernetes configuration
#     config.load_kube_config()

#     # Create a Kubernetes API client instance
#     api_instance = client.CustomObjectsApi()

#     # Create the custom resource in the cluster
#     api_instance.create_namespaced_custom_object(
#         group="infrastructure.cluster.x-k8s.io",
#         version="v1alpha1",
#         namespace="ha-vcluster",
#         plural="vclusters",
#         body=custom_resource2
#     )
# @app.get("/vclusters/{namespace}/{name}")
# def read_vcluster(namespace: str, name: str):
#     try:
#         # Get the vcluster resource
#         vcluster = custom_object_api.get_namespaced_custom_object(
#             group="infrastructure.cluster.x-k8s.io",
#             version="v1alpha1",
#             namespace=namespace,
#             plural="vclusters",
#             name=name
#         )
#         return vcluster
#     except client.rest.ApiException as e:
#         return {"error": e.reason}

# @app.delete("/vclusters/{namespace}/{name}")
# def delete_vcluster(namespace: str, name: str):
#     try:
#         # Delete the vcluster resource
#         custom_object_api.delete_namespaced_custom_object(
#             group="infrastructure.cluster.x-k8s.io",
#             version="v1alpha1",
#             namespace=namespace,
#             plural="vclusters",
#             name=name,
#             body=client.V1DeleteOptions()
#         )
#         return {"message": "vcluster deleted successfully"}
#     except client.rest.ApiException as e:
#         return {"error": e.reason}