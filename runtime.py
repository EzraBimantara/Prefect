from prefect import flow, task, runtime

@flow(log_prints= True)
def my_flow(x):
    print ("My name is ", runtime.flow_run.name)
    print(" I belong to deployment", runtime.deployment.name)
    my_task(2)

@task 
def my_task(y):
    print ("My name is ", runtime.task_run.name)
    print(" flow run parameter", runtime.flow_run.parameters)


if __name__ == "__main__":
    my_flow(2)