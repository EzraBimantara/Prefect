import httpx
from prefect import flow, task, get_run_logger, runtime
from prefect.blocks.system import Secret
import random
import time

@task(retries=3, retry_delay_seconds=5)
def fetch_weather(lat: float, lon: float):
    logger = get_run_logger()
    base_url = "https://api.open-meteo.com/v1/forecast/"
    
    if random.choice([True, False]):
        logger.warning("DEMO: Memaksa kegagalan untuk tes retry...")
        raise Exception("Kegagalan paksaan!")

    temps = httpx.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    
    forecasted_temp = float(temps.json()["hourly"]["temperature_2m"][0])
    logger.info(f"Forecasted temp C: {forecasted_temp} degrees")
    
    return forecasted_temp

@task
def save_weather(temp: float):
    with open("weather.csv", "w+") as w:
        w.write(str(temp))
    return "Successfully wrote temp"

@flow(log_prints=True)
def pipeline(lat: float = -7.2881839, lon: float = 112.8165095):
    
    logger = get_run_logger()

    logger.info(f"===== SELAMAT DATANG DI LAB 102 =====")
    logger.info(f"Menjalankan flow run dengan nama: {runtime.flow_run.name}")

    logger.info("Mencoba memuat 'Secret' block bernama 'my-api-key'...")
    secret_block = Secret.load("my-api-key")
    secret_value = secret_block.value.get_secret_value()    
    logger.info(f"Berhasil memuat secret! Nilainya dimulai dengan: {secret_value[:3]}...")

    temp = fetch_weather(lat, lon)
    result = save_weather(temp)
    
    logger.info(f"Flow selesai dengan hasil: {result}")
    return result

if __name__ == "__main__":
    pipeline()