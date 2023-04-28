import yaml
from kubernetes import client, config

def create():
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
    

def read():
    # Load Kubernetes configuration
    config.load_kube_config()

    # Create a Kubernetes API client instance
    api_instance = client.CustomObjectsApi()

    # Get the custom resources in the cluster
    clusters = api_instance.list_namespaced_custom_object(
        group="cluster.x-k8s.io",
        version="v1beta1",
        namespace="ha-vcluster",
        plural="clusters"
    )

    vclusters = api_instance.list_namespaced_custom_object(
        group="infrastructure.cluster.x-k8s.io",
        version="v1alpha1",
        namespace="ha-vcluster",
        plural="vclusters"
    )

    # Print the custom resources
    print(clusters)
    print(vclusters)

def delete():
    # Load Kubernetes configuration
    config.load_kube_config()

    # Create a Kubernetes API client instance
    api_instance = client.CustomObjectsApi()

    # Delete the custom resources from the cluster
    api_instance.delete_namespaced_custom_object(
        group="infrastructure.cluster.x-k8s.io",
        version="v1alpha1",
        namespace="ha-vcluster",
        plural="vclusters",
        name="ha-vc"
    )

    api_instance.delete_namespaced_custom_object(
        group="cluster.x-k8s.io",
        version="v1beta1",
        namespace="ha-vcluster",
        plural="clusters",
        name="ha-vc"
    )
if __name__ == "__main__":
    operation = input("Enter operation (create, delete, read): ")
    
    
    



    if operation == "create":
        create()
        # list_cluster()
        # cluster_name = input("Enter cluster name: ")
    elif operation == "delete":
         delete()
    elif operation == "read":
         read()
         
        



