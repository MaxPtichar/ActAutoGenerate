from datetime import datetime

import flet as ft

import doc_engine
from models import Organization, Requisites


class OrgFormDialogAlert(ft.AlertDialog):
    def __init__(self, on_save):
        super().__init__()

        self.callback_on_save = on_save

        # организация
        self.name = ft.TextField(
            label="Название организации",
            hint_text="ПримерТехно",
            tooltip="Сокращенное название организации",
        )
        self.manager_name = ft.TextField(
            label="Имя руководителя", hint_text="Иванов Иван Иванович"
        )
        self.agreement = ft.TextField(
            label="Договор", hint_text="№ 123-А от 01.01.2026"
        )
        self.fee = ft.TextField(
            label="Стоимость услуг",
            hint_text="500.00",
            keyboard_type=ft.KeyboardType.NUMBER,
        )
        self.act_counter = ft.TextField(
            label="Номер акта",
            value="1",
            tooltip="Отсчет актов начнется с введенного номера",
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        self.date_field = ft.TextField(
            label="Дата",
            hint_text="01.01.2026",
            tooltip="Созданный акт будет последним числом введенного месяца",
        )

        # Реквизиты (Requisites)
        self.unp = ft.TextField(
            label="УНП",
            hint_text="9 цифр",
            keyboard_type=ft.KeyboardType.NUMBER,
            max_length=9,
        )
        self.address = ft.TextField(
            label="Адрес", hint_text="г. Минск, ул. Центральная, д. 1"
        )
        self.bank_account = ft.TextField(
            label="Расчетный счет (IBAN)", hint_text="BY20XXXX...", max_length=28
        )
        self.name_of_bank = ft.TextField(
            label="Название банка", hint_text="ОАО 'Приорбанк'"
        )
        self.bic = ft.TextField(label="БИК банка", hint_text="8 символов", max_length=8)
        self.mobile_num = ft.TextField(
            label="Моб. номер", hint_text="+375...", keyboard_type=ft.KeyboardType.PHONE
        )
        self.e_mail = ft.TextField(label="E-mail", hint_text="example@mail.com")

        # контент окна

        self.content = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        [
                            ft.Text("Организация"),
                            self.name,
                            self.manager_name,
                            self.agreement,
                            self.fee,
                            self.act_counter,
                            self.date_field,
                        ]
                    ),
                    ft.VerticalDivider(),
                    ft.Column(
                        [
                            ft.Text("Реквизиты"),
                            self.unp,
                            self.address,
                            self.bank_account,
                            self.name_of_bank,
                            self.bic,
                            self.mobile_num,
                            self.e_mail,
                        ]
                    ),
                ]
            )
        )

        self.actions = [
            ft.TextButton("Сохранить", on_click=self.save_data),
            ft.TextButton("Назад", on_click=self.close_dialog),
        ]

    def get_all_data(self) -> Organization:
        reqs = Requisites(
            unp=self.unp.value,
            address=self.address.value,
            bank_account=self.bank_account.value,
            name_of_bank=self.name_of_bank.value,
            bic=self.bic.value,
            mobile_num=self.mobile_num.value,
            e_mail=self.e_mail.value,
        )
        return Organization(
            id=None,
            name=self.name.value,
            manager_name=self.manager_name.value,
            agreement=self.agreement.value,
            fee=float(self.fee.value),
            act_counter=int(self.act_counter.value),
            date=datetime.strptime(self.date_field.value, "%d.%m.%Y").date(),
            requisites=reqs,
        )

    def close_dialog(self, e):
        self.open = False
        self.page.update()

    def save_data(self, e):
        try:
            obj = self.get_all_data()
            self.callback_on_save(obj)
            self.close_dialog(e)

        except Exception as ex:
            self.page.show_dialog(ft.SnackBar(ft.Text(f"Ошибка {ex}")))


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
            doc_engine.create_files()

            self.page.show_dialog(ft.SnackBar(ft.Text("Акты созданы.")))
        except Exception as ex:
            self.page.show_dialog(ft.SnackBar(ft.Text(f"Ошибка. {ex}")))

        self.gen_button.disabled = False
        self.page.update()


def main(page: ft.Page):

    def handle_save(new_org: Organization):
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


if __name__ == "__main__":
    ft.app(target=main)
