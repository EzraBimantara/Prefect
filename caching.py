from prefect import task
from prefect.cache_policies import INPUTS
from datetime import timedelta

@task(cache_policy=INPUTS , log_prints= True, cache_expiration=timedelta(minutes=1))
def my_cached_task(x : int):
    print(f"Result is : {x+42}")


my_cached_task(8)
my_cached_task(8)
my_cached_task(33)