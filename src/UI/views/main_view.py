import asyncio
from pathlib import Path
from typing import Awaitable, Callable

import flet as ft

from src.models import Organization
from src.services.document_services import DocumentService
from src.services.Flet_client_storage import PathStorage
from src.services.organization_services import OrgServices
from src.UI.components.OrgForm import OrgFormDialogAlert
from src.UI.views.organizations_view import ShowOrg


class MainMenuView(ft.Column):
    def __init__(
        self,
        doc_service: DocumentService,
        on_add_org: Callable[[], None],
        on_show_org: Callable[[], None],
        on_open_directory: Callable[[ft.ControlEvent], Awaitable[None]],
    ):
        super().__init__()
        self.on_open_directory = on_open_directory
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
            ft.TextButton(
                "Выбрать шаблон",
                icon=ft.Icons.DIRECTIONS,
                on_click=lambda e: asyncio.create_task(self.on_open_directory(e)),
            ),
        ]

    def _generate_docs(self, e):
        temp_path = Path(self.doc_service.template_path)
        if not temp_path.exists():
            dialog_alert_ok = ft.AlertDialog(
                content=ft.Text(f"Для продолжения выберите шаблон"),
                actions=[
                    ft.TextButton(
                        "Выбрать шаблон...",
                        icon=ft.Icons.FILE_OPEN,
                        on_click=lambda e: asyncio.create_task(
                            self.on_open_directory(e)
                        ),
                    ),
                    ft.TextButton("Отмена", on_click=lambda e: self.page.pop_dialog()),
                ],
            )
            self.page.show_dialog(dialog_alert_ok)
            return

        self.doc_service.generate_acts()
        self.page.show_dialog(ft.SnackBar(ft.Text(f"Акты созданы")))


async def build_app(page: ft.Page) -> None:

    doc_service = DocumentService()
    organization_service = OrgServices()
    fcs = PathStorage(page, doc_service)

    await fcs.get_path()

    page.title = "Генератор актов"

    def handle_save(new_org: Organization):
        organization_service.add_org(new_org)
        page.show_dialog(
            ft.SnackBar(ft.Text(f"Организация {new_org.name} успешно добавлена"))
        )

    org_dialog = OrgFormDialogAlert(org=None, on_save=handle_save)

    def show_main_menu():
        page.controls.clear()
        page.add(main_menu)

    def show_org_list():
        page.controls.clear()
        page.add(ShowOrg(organization_service, on_back=show_main_menu))

    async def open_directory(e):

        files = await ft.FilePicker().pick_files(allow_multiple=False)

        if not files:
            return
        template_path = files[0].path
        await fcs.save_path(template_path)
        # doc_service.get_path_for_generate(template_path)

    main_menu = MainMenuView(
        doc_service=doc_service,
        on_add_org=lambda: page.show_dialog(org_dialog),
        on_show_org=show_org_list,
        on_open_directory=open_directory,
    )

    show_main_menu()
