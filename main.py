from fastapi import FastAPI, Request, Response
from routers import webhook
from db import create_all_tables
from services.whatsAppService import WhatsAppService

app = FastAPI(
    title="Asistente virtual de NEST", 
    description="Bot de Agencia NEST", 
    lifespan=create_all_tables
    )
app.include_router(webhook.router)

@app.get("/")
async def root():
    return Response(content="Bienvenido al Bot de NEST", media_type="text/plain")
    
