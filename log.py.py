from prefect import flow, get_run_logger

@flow(name= "log_example")
def log_it():
    logger = get_run_logger()
    logger.info("this is an info log")
    logger.debug("this is a debuglog")

if __name__ == "__main__":
    log_it()