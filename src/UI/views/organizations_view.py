from typing import Callable

import flet as ft

from src.services.organization_services import OrgServices
from src.UI.elements.organization_table import OrganizationTable


class ShowOrg(ft.Column):
    def __init__(self, org_service: OrgServices, on_back: Callable[[], None]):
        super().__init__()
        self.org = org_service
        self.on_back = on_back

        self.table = OrganizationTable(
            org_service, self._on_edit_org, self._on_delete_org
        )
        self.controls = [self._header(), self.table]

    def _header(self):
        return ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.ARROW_BACK, on_click=lambda e: self.on_back()
                ),
                ft.Text("Организации", size=20),
            ]
        )

    def _on_edit_org(self, org: Organization):
        print("Edit:", org.name)

    def _on_delete_org(self, org: Organization):
        print("Delete:", org.name)
