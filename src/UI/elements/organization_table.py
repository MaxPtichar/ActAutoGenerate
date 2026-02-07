from typing import Callable

import flet as ft

from src.models import Organization
from src.services.organization_services import OrgServices
from src.UI.elements.Popup_Menu_Button import ActionMenu


class OrganizationTable(ft.Container):
    def __init__(
        self,
        org_service: OrgServices,
        on_edit: Callable[[Organization], None],
        on_delete: Callable[[Organization], None],
    ) -> None:
        super().__init__()
        self.org_service = org_service
        self.on_edit = on_edit
        self.on_delete = on_delete

        self.content = self.build_columns()

    def build_columns(self):
        return ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("Название")),
                ft.DataColumn(label=ft.Text("УНП")),
                ft.DataColumn(label=ft.Text("Доход")),
                ft.DataColumn(label=ft.Text("")),
            ],
            rows=self._build_rows(),
        )

    def _build_rows(self):
        rows = []
        for org in self.org_service.list_all():
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(org.name)),
                        ft.DataCell(ft.Text(org.requisites.unp)),
                        ft.DataCell(ft.Text(f"{int(org.fee)}")),
                        ft.DataCell(
                            ActionMenu(
                                org=org,
                                on_update=self.on_edit,
                                on_delete=self.on_delete,
                            )
                        ),
                    ]
                )
            )

        return rows
