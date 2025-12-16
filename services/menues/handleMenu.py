from ..whatsAppService import WhatsAppService
from ..odooService import OdooService
from fastapi import Response
from ..geminiService import GeminiService
from db import SessionDep
from sqlmodel import select

# Controlador del chat
class HandleMenu:
    async def handleMenuOption(self, session, user_pointer, sender_data, option_id, to):
        message_reply   = "Disculpe, no he entendido tu respuesta"
        wa_id           = sender_data.get("wa_id", None)

        if option_id == 'desactivar_campañas':
            message_reply   = f"Entendemos su decisión, por eso, de ahora en adelante no recibirá más mensajes de nuestra agencia, a menos que cambie de opinión.\n\nEn caso de querer activar este medio para comunicaciones, escriba la palabra *volver* y lo reactivaremos."
            await OdooService.request_update(wa_id, "INACTIVO")
        elif option_id == 'activar_campañas':
            message_reply   = "¡Perfecto! Recibirá mensajes sobre anuncios de nuestra agencia de aquí en adelante ☺."
            await OdooService.request_update(wa_id, "ACTIVO")
        elif option_id == "prefiero_no":
            message_reply   = "Entiendo, el equipo estará atento cualquier novedad.\n\nGracias por comunicarse con NEST Agencia Educativa 🟢."

        await WhatsAppService.sendWhatsappMessage(to, message_reply)
        

    async def sendMenuDesert(self, message_from):
        menu_message = "¿Desea seguir en comunicación?"
        buttons = [
            {
                "type": "reply",
                "reply": {
                    "id": "desactivar_campañas",
                    "title": "No recibir mensajes"
                }
            },
            {
                "type": "reply",
                "reply": {
                    "id": "activar_campañas",
                    "title": "Mantenerme activo"
                }
            }
        ]
        await WhatsAppService.sendInteractiveButtons(message_from, menu_message, buttons)


    async def sendMenuConfirm(self, message_from):
        menu_message = "Por favor, elija una opción"
        buttons = [
            {
                "type": "reply",
                "reply": {
                    "id": "activar_campañas",
                    "title": "Si quiero"
                }
            },
            {
                "type": "reply",
                "reply": {
                    "id": "prefiero_no",
                    "title": "Prefiero no"
                }
            }
        ]
        await WhatsAppService.sendInteractiveButtons(message_from, menu_message, buttons)