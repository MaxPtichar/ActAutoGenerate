from typing import Callable

import flet as ft

from src.models import Organization


class ActionMenu(ft.PopupMenuButton):
    def __init__(
        self,
        org: Organization,
        on_update: Callable[[Organization], None],
        on_delete: Callable[[Organization], None],
    ):
        super().__init__()
        self.org = org
        self.on_update = on_update
        self.on_delete = on_delete

        self.icon = ft.Icons.MORE_VERT

        self.update_popup = ft.PopupMenuItem(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.EDIT_OUTLINED),
                    ft.Text("Update"),
                ]
            ),
            on_click=self._handle_edit_click,
        )

        self.delete_popup = ft.PopupMenuItem(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.DELETE_OUTLINE, color=ft.Colors.RED),
                    ft.Text("Delete", color=ft.Colors.RED),
                ]
            ),
            on_click=self._handle_delete_click,
        )

        self.items = [self.update_popup, ft.PopupMenuItem(), self.delete_popup]

    def _handle_edit_click(self, e):

        if self.on_update:
            self.on_update(self.org)

    def _handle_delete_click(self, e):

        if self.on_delete:
            self.on_delete(self.org)
