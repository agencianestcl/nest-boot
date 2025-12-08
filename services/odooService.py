import os
import xmlrpc.client
from .httpRequets import HttpRequest
from typing import Optional, Dict, Any
from dotenv import load_dotenv

load_dotenv()

class OdooService:
    url      = os.getenv("URL_ODOO")
    db       = os.getenv("DB_ODOO")
    username = os.getenv("USERNAME_ODOO")
    password = os.getenv("PASS_ODOO")

    @staticmethod
    async def request_update(wa_id, update_value):
        phone_code = wa_id[-6:]
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(OdooService.url))
        uid    = common.authenticate(OdooService.db, OdooService.username, OdooService.password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(OdooService.url))
        records = models.execute_kw(OdooService.db, uid, OdooService.password, 'res.partner', 'search_read', [[['phone', 'ilike', phone_code], ['phone', '!=', False]]], {'fields': ['x_studio_habilitado_para_campanas_wa', 'phone', 'id'], 'limit': 1})
        user_id = records[0].get("id", 0)
        models.execute_kw(OdooService.db, uid, OdooService.password, 'res.partner', 'write', [[user_id], {'x_studio_habilitado_para_campanas_wa': update_value}])

