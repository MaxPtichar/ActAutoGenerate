from datetime import datetime
from typing import Callable

import flet as ft

from src.models import Organization, Requisites
from src.UI.elements.inputs import AppTextField


class OrgFormDialogAlert(ft.AlertDialog):
    def __init__(
        self, on_save: Callable[[Organization], None], org: Organization | None = None
    ):
        super().__init__()

        self.callback_on_save = on_save

        self.current_org_id = org.id if org else None

        # организация
        self.name = AppTextField(
            label="Название организации",
            value=org.name if org else "",
            hint="ПримерТехно",
            tooltip="Сокращенное название организации",
        )

        self.manager_name = AppTextField(
            label="Имя руководителя",
            value=org.manager_name if org else "",
            hint="Иванов Иван Иванович",
        )

        self.agreement = AppTextField(label="Договор", hint="№ 123-А от 01.01.2026")

        self.fee = AppTextField(
            label="Стоимость услуг",
            value=org.fee if org else 0,
            hint="500.00",
            is_numer=True,
        )

        self.act_counter = AppTextField(
            label="Номер акта",
            value=org.act_counter if org else 0,
            hint="1",
            tooltip="Отсчет актов начнется с введенного номера",
            is_numer=True,
        )

        self.date_field = AppTextField(
            label="Дата",
            value=(
                org.date.strftime("%d.%m.%Y")
                if org
                else datetime.today().strftime("%d.%m.%Y")
            ),
            hint="01.01.2026",
            tooltip="Созданный акт будет последним числом введенного месяца",
        )

        # Реквизиты (Requisites)
        self.unp = AppTextField(
            label="УНП",
            value=org.requisites.unp if org else "",
            hint="9 цифр",
            keyboard_type=ft.KeyboardType.NUMBER,
            max_length=9,
        )
        self.address = AppTextField(
            label="Адрес",
            value=org.requisites.address if org else "",
            hint="г. Минск, ул. Центральная, д. 1",
        )
        self.bank_account = AppTextField(
            label="Расчетный счет (IBAN)",
            value=org.requisites.bank_account if org else "",
            hint="BY20XXXX...",
            max_length=28,
        )
        self.name_of_bank = AppTextField(
            label="Название банка",
            value=org.requisites.name_of_bank if org else "",
            hint="ОАО 'Приорбанк'",
        )

        self.bic = AppTextField(
            label="БИК банка",
            value=org.requisites.bic if org else "",
            hint="8 символов",
            max_length=8,
        )

        self.mobile_num = AppTextField(
            label="Моб. номер",
            value=org.requisites.mobile_num if org else "",
            hint="+375...",
            is_numer=True,
        )
        self.e_mail = AppTextField(
            label="E-mail",
            value=org.requisites.e_mail if org else "",
            hint="example@mail.com",
        )

        # контент окна

        self.content = ft.Container(
            content=ft.Row(
                scroll=ft.ScrollMode.AUTO,
                controls=[
                    ft.Column(
                        [
                            ft.Text(
                                "Организация",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.PRIMARY,
                                text_align=ft.TextAlign.CENTER,
                                width=300,
                            ),
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
                            ft.Text(
                                "Реквизиты",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.PRIMARY,
                                text_align=ft.TextAlign.CENTER,
                                width=300,
                            ),
                            self.unp,
                            self.address,
                            self.bank_account,
                            self.name_of_bank,
                            self.bic,
                            self.mobile_num,
                            self.e_mail,
                        ]
                    ),
                ],
            )
        )

        self.actions = [
            ft.TextButton(
                "Сохранить",
                on_click=self.save_data,
            ),
            ft.TextButton("Назад", on_click=self.close_dialog),
        ]

    def collect_raw_data(self) -> dict:
        return {
            "id": self.current_org_id,
            "name": self.name.value,
            "manager_name": self.manager_name.value,
            "agreement": self.agreement.value,
            "fee": self.fee.value,
            "act_counter": self.act_counter.value,
            "date": self.date_field.value,
            "unp": self.unp.value,
            "address": self.address.value,
            "bank_account": self.bank_account.value,
            "name_of_bank": self.name_of_bank.value,
            "bic": self.bic.value,
            "mobile_num": self.mobile_num.value,
            "e_mail": self.e_mail.value,
        }

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
            id=self.current_org_id,
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
