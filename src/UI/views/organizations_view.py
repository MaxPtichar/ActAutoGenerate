from typing import Callable

import flet as ft

from src.services.organization_services import OrgServices


class ShowOrg(ft.Column):
    def __init__(self, org_service: OrgServices, on_back: Callable[[], None]):
        super().__init__()
        self.org = org_service
        self.on_back = on_back

        self.controls = [self._header(), self._org_list()]

    def _header(self):
        return ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.ARROW_BACK, on_click=lambda e: self.on_back()
                ),
                ft.Text("Организации", size=20),
            ]
        )

    def _org_list(self):
        lv = ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("Название")),
                ft.DataColumn(label=ft.Text("УНП")),
                ft.DataColumn(label=ft.Text("Доход")),
                ft.DataColumn(label=ft.Text("Настройки")),
            ],
            rows=[],
        )

        for org in self.org.list_all():
            lv.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(org.name)),
                        ft.DataCell(ft.Text(org.requisites.unp)),
                        ft.DataCell(ft.Text(f"{int(org.fee)}")),
                        ft.DataCell(ft.IconButton(ft.CupertinoIcons.ELLIPSIS_VERTICAL)),
                    ]
                )
            )

        return lv
