from sagemaker.sklearn import SKLearn
from sagemaker import get_execution_role

role = get_execution_role()

sklearn = SKLearn(
    entry_point='train.py',
    role=role,
    instance_count=1,
    instance_type='ml.m5.large',
    framework_version='1.2-1',
    py_version='py3'
)

sklearn.fit()
sklearn.deploy(instance_type='ml.t2.medium', initial_instance_count=1)
