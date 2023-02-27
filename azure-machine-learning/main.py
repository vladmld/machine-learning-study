from azureml.core import Workspace
from azureml.core import Experiment

ws = Workspace.from_config('./azure-machine-learning/config.json')

for compute_name in ws.compute_targets:
    compute = ws.compute_targets[compute_name]
    print(compute.name, ":", compute)