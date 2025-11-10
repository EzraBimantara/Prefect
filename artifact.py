import httpx
from prefect import flow, task
from prefect.artifacts import create_markdown_artifact

@task
def report(temp):
    markdown_report = f"""
# Weather Report
The forecasted temperature is **{temp}** degrees Celsius.
"""
    create_markdown_artifact(
        key="weather-report",
        markdown=markdown_report,
        description="A simple weather report",
    )
    
