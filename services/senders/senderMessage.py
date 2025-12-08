from ..whatsAppService import WhatsAppService
from typing import Optional, List, Dict, Any

class SenderMessage:
    async def sendProcessingMessage(self, message_from, message_id):
        await WhatsAppService.sendWhatsappMessage(message_from, "Pensando 🧠", message_id)


    async def sendListeningMessage(self, message_from, message_id):
        await WhatsAppService.sendWhatsappMessage(message_from, "Escuchando👂🏽", message_id)


    async def sendViewImage(self, message_from, message_id):
        await WhatsAppService.sendWhatsappMessage(message_from, "Analizando la imagen 👀", message_id)


    async def sendWelcomeMessage(self, message_from, sender_name):
        message = f"*Hola {sender_name}*, un gusto en saludar.\n\n ¿Qué le gustaría hacer?"
        await WhatsAppService.sendWhatsappMessage(message_from, message)


    async def sendCurrentMessage(self, message_from):
        message = f"Puedo ayudarle buscando una forma de hacer amena la comunicación con la agencia.\n\nPara seguir recibiendo nuestros mensajes con información relevante marque la opción: 'Mantenerme activo', de lo contrario marque la opción: 'No recibir mensajes'."
        await WhatsAppService.sendWhatsappMessage(message_from, message)


    async def sendReactivateMessage(self, message_from):
        message = f"¡Hola! Nos complace saludarle de nuevo, vemos que ha escrito la palabra clave para volver a reactivar las notificaciones automáticas de parte de nuestra agencia\n\n ¿Desea reactivar este medio para recibir mensajes de la agencia?"
        await WhatsAppService.sendWhatsappMessage(message_from, message)