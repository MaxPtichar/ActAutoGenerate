import flet as ft

from src.models import Organization
from src.services.document_services import DocumentService
from src.services.organization_services import OrgServices
from src.UI.components.OrgForm import OrgFormDialogAlert
from src.UI.elements.buttons import MainMenuButton, ShowOrg


def build_app(page: ft.Page) -> None:
    doc_service = DocumentService()
    organization_service = OrgServices()

    def handle_save(new_org: Organization):
        organization_service.add_org(new_org)
        page.show_dialog(
            ft.SnackBar(ft.Text(f"Организация {new_org.name} успешно добавлена"))
        )

    org_dialog = OrgFormDialogAlert(on_save=handle_save)

    gen_act = MainMenuButton(doc_service)
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

    show_org = ShowOrg(organization_service)
    page.add(show_org)


if __name__ == "__main__":
    ft.app(target=main)
