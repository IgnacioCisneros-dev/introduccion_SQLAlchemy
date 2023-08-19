from fastapi import FastAPI
from routers import productos

app = FastAPI(title='Control de empleados.',
              description='API que ayuda a la gestion y control de los colaboradores de la empresa.',
              version='0.0.1')

app.include_router(productos.router_productos)