from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source = "https://github.com/EzraBimantara/Prefect.git",
        entrypoint="103task.py:pipeline",
    ).deploy(
        name="lab-103-deploy-hybrid",
        work_pool_name="HybridWork",
    )