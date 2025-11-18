from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source = "https://github.com/EzraBimantara/Prefect.git",
        entrypoint="machinelearning.py:ml_workflow",
    ).deploy(
        name="lab-103-deploy",
        work_pool_name="pi52-harada",
        job_variables={"pip_packages": ["pandas", "scipy", "scikit-learn"]}
    )