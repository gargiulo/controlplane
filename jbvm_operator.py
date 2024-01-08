# This code creates a K8S Operator which will populate an object of kind 'JBVM' with two additional fields: 
# - cmdbname
# - deploystatus
# Run it with: "kopf run jbvm_operator.py --verbose"

# Use the following command to test: 
# "kubectl get jbvms -o custom-columns=NAME:.metadata.name,CMDBNAME:.spec.cmdbname,DEPLOYMENT:.spec.deploystatus"

import kopf
from kubernetes import client, config

# Define the handler function for the operator.
@kopf.on.create('jbvms')
def handle_create(namespace, body, **kwargs):
    # Get the name of the custom resource.
    name = body['metadata']['name']
    
    # Update the "cmdbname" property of the custom resource.
    api = client.CustomObjectsApi()
    api.patch_namespaced_custom_object(
        group='jb.com',
        version='v1',
        namespace=namespace,
        plural='jbvms',
        name=name,
        body={
            'spec': {
                'cmdbname': 'srp12345lx',
                'deploystatus': 'pending'
            }
        }
    )