import ee
from config import EE_PROJECT_ID

print("Autenticando no Earth Engine...")
ee.Authenticate()

print("Inicializando Earth Engine...")
ee.Initialize(project=EE_PROJECT_ID)

print("Earth Engine inicializado com sucesso!")