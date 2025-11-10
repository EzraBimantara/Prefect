import httpx
from prefect import flow, task, get_run_logger, runtime
from prefect.artifacts import create_markdown_artifact
from prefect.blocks.system import Secret
from prefect.cache_policies import INPUTS, DEFAULT
from datetime import timedelta, datetime
import random
import time

@task(
    persist_result=True, 
    cache_policy=DEFAULT, 
    cache_expiration=timedelta(minutes=10)
)
def fetch_weather(lat: float, lon: float):
    logger = get_run_logger()
    base_url = "https://api.open-meteo.com/v1/forecast/"

    temps = httpx.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    
    forecasted_temp = float(temps.json()["hourly"]["temperature_2m"][0])
    logger.info(f"Forecasted temp C: {forecasted_temp} degrees")
    
    logger.info("Membuat Markdown Artifact...")
    markdown_report = f"""
    # Laporan Cuaca
    Prakiraan cuaca untuk lokasi (lat: {lat}, lon: {lon}).

    | Deskripsi | Nilai |
    |:---|:---|
    | **Suhu Saat Ini** | **{forecasted_temp} °C** |
    | Waktu Laporan | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} |
    """
    
    create_markdown_artifact(
        key="laporan-cuaca",
        markdown=markdown_report,
        description="Laporan cuaca harian."
    )
    
    

@flow
def pipeline(lat: float = -7.28, lon: float = 112.81):
    fetch_weather(lat, lon)

if __name__ == "__main__":
    pipeline()