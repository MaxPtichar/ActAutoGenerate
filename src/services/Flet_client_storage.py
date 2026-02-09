import json
import os
from pathlib import Path

import flet as ft

from src.services import document_services
from src.services.document_services import DocumentService


class PathStorage:

    TEMPLATE_KEY = "template_path"

    def __init__(self, page: ft.Page, dc: DocumentService):
        self.dc = dc
        self.page = page

    async def get_path(self):
        templ_path = await self.page.shared_preferences.get(self.TEMPLATE_KEY)
        if not templ_path:
            return
        self.dc.get_path_for_generate(templ_path)

    async def save_path(self, temp_path):
        print(temp_path)
        try:
            await self.page.shared_preferences.set(self.TEMPLATE_KEY, temp_path)
        except Exception as e:
            print(f"Error {e}")
