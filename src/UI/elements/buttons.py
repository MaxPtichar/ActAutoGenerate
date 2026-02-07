import flet as ft

from src.services.document_services import DocumentService
from src.services.organization_services import OrgServices


class MainMenuButton(ft.Column):
    def __init__(self, doc_services: DocumentService):
        super().__init__()
        self.doc_services = doc_services

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.gen_button = ft.Button(
            content=ft.Text("Сгенерировать акты"),
            icon=ft.Icon(ft.Icons.DESCRIPTION),
            on_click=self.start_generation,
        )

        self.controls = [self.gen_button]

    def start_generation(self, e):
        self.gen_button.disabled = True
        self.gen_button.update()

        try:
            self.doc_services.generate_acts()

            self.page.show_dialog(ft.SnackBar(ft.Text("Акты созданы.")))
        except Exception as ex:
            self.page.show_dialog(ft.SnackBar(ft.Text(f"Ошибка. {ex}")))

        self.gen_button.disabled = False
        self.page.update()


class ShowOrg(ft.Column):
    def __init__(self, org_service: OrgServices):
        super().__init__()
        self.org_service = org_service

        self.lv = ft.ListView(expand=1, spacing=10, padding=20, visible=False)

        self.show_org_button = ft.Button(
            content="Посмотреть организации",
            icon=ft.Icon(ft.Icons.WORK),
            on_click=self.page_add,
        )
        self.controls = [self.show_org_button, self.lv]

    def page_add(self, e):
        self.refresh_data()
        self.lv.visible = not self.lv.visible
        self.page.update()
        self.show_org_button = ft.ListView

    def refresh_data(self):
        data = self.org_service.list_all()
        self.lv.controls.clear()
        for row in data:
            self.lv.controls.append(ft.Text(f"{row.name}"))
