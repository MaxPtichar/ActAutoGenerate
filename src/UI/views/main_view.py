from typing import Callable

import flet as ft

from src.models import Organization
from src.services.document_services import DocumentService
from src.services.organization_services import OrgServices
from src.UI.components.OrgForm import OrgFormDialogAlert
from src.UI.elements.buttons import MainMenuButton
from src.UI.views.organizations_view import ShowOrg


class MainMenuView(ft.Column):
    def __init__(
        self,
        doc_service: DocumentService,
        on_add_org: Callable[[], None],
        on_show_org: Callable[[], None],
    ):
        super().__init__()
        self.doc_service = doc_service

        self.controls = [
            ft.TextButton(
                "Сгенерировать акты",
                icon=ft.Icons.DESCRIPTION,
                on_click=self._generate_docs,
            ),
            ft.TextButton(
                "Добавить организацию",
                icon=ft.Icons.CORPORATE_FARE,
                on_click=lambda e: on_add_org(),
            ),
            ft.TextButton(
                "Показать организации",
                icon=ft.Icons.WORK,
                on_click=lambda e: on_show_org(),
            ),
        ]

    def _generate_docs(self, e):
        self.doc_service.generate_acts()


def build_app(page: ft.Page) -> None:
    doc_service = DocumentService()
    organization_service = OrgServices()

    page.title = "Генератор актов"

    def handle_save(new_org: Organization):
        organization_service.add_org(new_org)
        page.show_dialog(
            ft.SnackBar(ft.Text(f"Организация {new_org.name} успешно добавлена"))
        )

    org_dialog = OrgFormDialogAlert(on_save=handle_save)

    def show_main_menu():
        page.controls.clear()
        page.add(main_menu)

    def show_org_list():
        page.controls.clear()
        page.add(ShowOrg(organization_service, on_back=show_main_menu))

    main_menu = MainMenuView(
        doc_service=doc_service,
        on_add_org=lambda: page.show_dialog(org_dialog),
        on_show_org=show_org_list,
    )

    show_main_menu()
