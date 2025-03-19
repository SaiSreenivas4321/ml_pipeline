from pathlib import Path

#D:\Mlops_eur\ml_pipeline\config\config.yaml
#ml_pipeline\ml_pipline\config_u\config.yaml

#D:\Mlops_eur\ml_pipeline\config
#ml_pipeline\config\config.yaml
#D:\Mlops_eur\ml_pipeline\ml_pipline\config_u\config.yaml
#CONFIG_FILE_PATH = Path(r"ml_pipeline\ml_pipeline\config_u\config.yaml")
#D:\Mlops_eur\ml_pipeline\ml_pipline\constants\__init__.py
#ml_pipeline\config\config.yaml

CONFIG_FILE_PATH = Path(r"ml_pipeline/config/config.yaml")
print(CONFIG_FILE_PATH,"config location")
PARAMS_FILE_PATH = Path("config/parmas.yaml")
SCHEMA_FILE_PATH = Path("config/schema.yaml")
# import os
# print("Current Working Directory:", os.getcwd())