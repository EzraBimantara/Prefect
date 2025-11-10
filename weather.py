
import httpx
from prefect import flow, task



@task
def fetch_weather(lat: float, lon: float ):
   
    base_url = "https://api.open-meteo.com/v1/forecast/"
    
    # Make the HTTP GET request using httpx
    temps = httpx.get(
        base_url,
        # Pass parameters for latitude, longitude, and the data we want
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    
    forecasted_temp = float(temps.json()["hourly"]["temperature_2m"][0])
    

    print(f"Forecasted temp C: {forecasted_temp} degrees")
    
    return forecasted_temp
@task
def save_weather (temp : float):
    with open ("weather.csv", "w+") as w:
        w.write(str(temp))
    return "Succesfully wrote temp"

@flow
def pipeline(lat: float = -7.2881839, lon: float = 112.8165095 ):
    temp=fetch_weather(lat, lon)
    result= save_weather(temp)
    return result



if __name__ == "__main__":
    #fetch_weather.serve(name="test-deploy")
    # This block allows you to run the flow directly
    # as a simple Python script (e.g., `python weather_flow.py`)
    # Prefect will still track this as a flow run!
    #fetch_weather()
    pipeline()
