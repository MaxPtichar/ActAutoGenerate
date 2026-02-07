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
                    ]
                )
            )

        return lv


# def _org_list(self):
#         lv = ft.ListView(expand=True, spacing=10)

#         for org in self.org.list_all():
#             lv.controls.append(
#                 ft.Row(
#                     controls=[
#                         ft.Text(f"Название: {org.name}", expand=True),
#                         ft.Text(f" УНП: {org.requisites.unp}", expand=True),
#                         ft.Text(f"Доход: {int(org.fee)}", expand=True),
#                     ]
#                 )
#             )

#         return lv
