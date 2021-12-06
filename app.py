from kubernetes import client, config

config.load_kube_config()

print("Hello world")

api = client.CustomObjectsApi()
k8s_nodes = api.list_cluster_custom_object("metrics.k8s.io", "v1beta1", "nodes")
k8s_pods = api.list_namespaced_custom_object("metrics.k8s.io", "v1beta1", "default", "pods")



for stats in k8s_nodes['items']:
    print("Node Name: %s\tCPU: %s\tMemory: %s" % (stats['metadata']['name'], stats['usage']['cpu'], stats['usage']['memory']))

for stats in k8s_pods['items']:
    print("Pod Name: %s\tCPU: %s\tMemory: %s" % (stats['metadata']['name'], stats['usage']['cpu'], stats['usage']['memory']))

