from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source = "https://github.com/EzraBimantara/Prefect.git",
        entrypoint="machinelearning.py:pipeline",
    ).deploy(
        name="lab-103-deploy",
        work_pool_name="Workpool",
    )