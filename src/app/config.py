import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "Sistema de Monitoramento Agricola"
VERSION = "0.1.0"

EE_PROJECT_ID = os.getenv("EE_PROJECT_ID")