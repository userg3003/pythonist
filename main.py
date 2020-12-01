from loguru import logger

from pythonist1 import primer as primer1
from pythonist2 import primer as primer2



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logger.info(f"----------------------")
    primer1()
    logger.info(f"======================")
    primer2()
    logger.info(f"======================")
