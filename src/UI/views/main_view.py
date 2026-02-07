from datetime import datetime

import flet as ft

from src.models import Organization
from src.services.document_services import DocumentService
from src.services.organization_services import OrgServices
from src.UI.components.OrgForm import OrgFormDialogAlert
from src.UI.elements.buttons import MainMenuButton, ShowOrg


def main(page: ft.Page) -> None:
    DocService = DocumentService()
    OrganizationService = OrgServices()

    def handle_save(new_org: Organization):
        OrganizationService.add_org(new_org)
        page.show_dialog(
            ft.SnackBar(ft.Text(f"Организация {new_org.name} успешно добавлена"))
        )

    org_dialog = OrgFormDialogAlert(on_save=handle_save)

    gen_act = MainMenuButton(DocService)
    page.title = "Генератор актов"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(gen_act)

    page.add(
        ft.Button(
            content=ft.Text("Добавить организацию"),
            icon=ft.Icon(ft.Icons.CORPORATE_FARE),
            on_click=lambda e: page.show_dialog(org_dialog),
        )
    )

    show_org = ShowOrg(OrganizationService)
    page.add(show_org)


if __name__ == "__main__":
    ft.app(target=main)
