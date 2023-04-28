from fastapi import FastAPI, HTTPException
import yaml
from kubernetes import client, config

app = FastAPI()

# Load Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client instance
api_instance = client.CoreV1Api()



@app.post("/create")
def create(namespace: str, name: str):
    namespace = f"{namespace}-vcluster"
    try:

        # Load the YAML file into a Python dictionary
        with open('cluster.yaml') as f:
            custom_resource = f.read().format(namespace=namespace, name=name)

        # Create the custom resource in the cluster
        api_instance = client.CustomObjectsApi()
        api_instance.create_namespaced_custom_object(
            group="cluster.x-k8s.io",
            version="v1beta1",
            namespace=namespace,
            plural="clusters",
            body=yaml.safe_load(custom_resource)
        )

        # Load the YAML file into a Python dictionary
        with open('vcluster.yaml') as f:
            custom_resource2 = f.read().format(namespace=namespace, name=name)


        # Create the custom resource in the cluster
        api_instance.create_namespaced_custom_object(
            group="infrastructure.cluster.x-k8s.io",
            version="v1alpha1",
            namespace=namespace,
            plural="vclusters",
            body=yaml.safe_load(custom_resource2)
        )
        return {"message": "vcluster created successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/vcluster/{namespace}/{name}")
def read_vcluster(namespace: str, name: str):
    namespace = f"{namespace}-vcluster"
    try:
        # Retrieve the vcluster object from the cluster
        api_instance = client.CustomObjectsApi()
        vcluster = api_instance.get_namespaced_custom_object(
            group="infrastructure.cluster.x-k8s.io",
            version="v1alpha1",
            namespace=namespace,
            plural="vclusters",
            name=name
        )

        return vcluster

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# @app.delete("/cluster/{namespace}/{name}")
# def delete_vcluster(namespace: str, name: str):
#     try:
#         # Delete the vcluster resource
#         custom_object_api = client.CustomObjectsApi()
#         custom_object_api.delete_namespaced_custom_object(
#             group="cluster.x-k8s.io",
#             version="v1beta1",
#             namespace=namespace,
#             plural="clusters",
#             name=name,
#             body=client.V1DeleteOptions()
#         )
#         return {"message": "cluster deleted successfully"}
#     except client.rest.ApiException as e:
#         return {"error": e.reason}
    
    
# @app.delete("/vclusters/{namespace}/{name}")
# def delete_vcluster(namespace: str, name: str):
#     try:
#         # Delete the vcluster resource
#         custom_object_api = client.CustomObjectsApi()
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

    
@app.delete("/namespace/{name}")
def delete_vcluster(name: str):
    name = f"{name}-vcluster"
    try:
        # Delete the vcluster resource
        api_instance.delete_namespace(name=name)
        return {"message": "vcluster deleted successfully"}
    except client.rest.ApiException as e:
        return {"error": e.reason}


