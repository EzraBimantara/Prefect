from prefect import task, flow
from prefect.transactions import transaction

@task
def write_file(contents:str):
    "writes to a file"
    with open("my_file.txt", "w") as f:
        f.write(contents)

@write_file.on_rollback
def delete_file(transaction):
    "Detels file"
    os.unlink("my_file.txt")

@task 
def quality_test():
    with open ("my_file.txt", "r") as f:
        data= f.readlines()
    if len (data) < 5:
        raise ValueError ("File content too short!")

@flow
def pipeline(contents:str):
    with transaction():
        write_file(contents)
        quality_test()
