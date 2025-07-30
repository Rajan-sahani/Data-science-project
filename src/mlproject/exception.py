import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))


from mlproject.loggers import logging

if __name__ == "__main__":
    try:
        logging.info("The execution has started")

       
        logging.info("The execution is running smoothly.")

    except Exception as e:
        logging.exception(f"An error occurred: {e}")
