from datetime import datetime

import flet as ft

from src.services.document_services import DocumentService
from src.services.organization_services import OrgServices
from src.UI.components.OrgForm import OrgFormDialogAlert

ds = DocumentService()
orgserv = OrgServices()


class MainMenuButton(ft.Column):
    def __init__(self):
        super().__init__()
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
            ds.generate_acts()

            self.page.show_dialog(ft.SnackBar(ft.Text("Акты созданы.")))
        except Exception as ex:
            self.page.show_dialog(ft.SnackBar(ft.Text(f"Ошибка. {ex}")))

        self.gen_button.disabled = False
        self.page.update()


class ShowOrg(ft.Column):
    def __init__(self):
        super().__init__()

        self.lv = ft.ListView(expand=1, spacing=10, padding=20, visible=False)

        self.show_org_button = ft.Button(
            content="Посмотреть организации",
            icon=ft.Icon(ft.Icons.WORK),
            on_click=self.page_add,
        )
        self.controls = [self.show_org_button, self.lv]

    def page_add(self, e):
        self.refgresh_data()
        self.lv.visible = not self.lv.visible
        self.page.update()
        self.show_org_button = ft.ListView

    def refgresh_data(self):
        data = orgserv.list_all()
        self.lv.controls.clear()
        for row in data:
            self.lv.controls.append(ft.Text(f"{row.name}"))


def main(page: ft.Page):

    def handle_save(new_org: Organization):
        orgserv.add_org(new_org)
        page.show_dialog(
            ft.SnackBar(ft.Text(f"Организация {new_org.name} успешно добавлена"))
        )

    org_dialog = OrgFormDialogAlert(on_save=handle_save)

    gen_act = MainMenuButton()
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

    show_org = ShowOrg()
    page.add(show_org)


if __name__ == "__main__":
    ft.app(target=main)
