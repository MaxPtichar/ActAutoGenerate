from datetime import datetime
from typing import Callable

import flet as ft

from src.models import Organization, Requisites
from src.services.organization_services import OrgServices
from src.UI.elements.inputs import AppTextField
from src.validators.org_validators import OrgValidator, ValidationError


class OrgFormDialogAlert(ft.AlertDialog):
    def __init__(
        self, on_save: Callable[[Organization], None], org: Organization | None = None
    ):
        super().__init__()

        self.callback_on_save = on_save

        self.current_org_id = org.id if org else None

        self.save_btn = ft.TextButton(
            "Сохранить",
            on_click=self.save_data,
            disabled=True,
        )

        # организация
        self.name = AppTextField(
            label="Название организации",
            value=org.name if org else "",
            hint="ПримерТехно",
            tooltip="Сокращенное название организации",
        )
        self.name.on_change = lambda e: self.on_change_handler(
            self.name, OrgValidator.validate_name_org
        )

        self.manager_name = AppTextField(
            label="Имя руководителя",
            value=org.manager_name if org else "",
            hint="Иванов Иван Иванович",
        )

        self.manager_name.on_change = lambda e: self.on_change_handler(
            self.manager_name, OrgValidator.validate_manager_name
        )

        self.agreement = AppTextField(label="Договор", hint="№ 123-А от 01.01.2026")

        self.agreement.on_change = lambda e: self.on_change_handler(
            self.agreement, OrgValidator.validate_agreement
        )

        self.fee = AppTextField(
            label="Стоимость услуг",
            value=org.fee if org else 0,
            hint="500.00",
            is_numer=True,
        )

        self.fee.on_change = lambda e: self.on_change_handler(
            self.fee, OrgValidator.validate_fee
        )

        self.act_counter = AppTextField(
            label="Номер акта",
            value=org.act_counter if org else 0,
            hint="1",
            tooltip="Отсчет актов начнется с введенного номера",
            is_numer=True,
        )

        self.act_counter.on_change = lambda e: self.on_change_handler(
            self.act_counter, OrgValidator.validate_act_counter
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

        self.date_field.on_change = lambda e: self.on_change_handler(
            self.date_field, OrgValidator.validate_date
        )

        # Реквизиты (Requisites)
        self.unp = AppTextField(
            label="УНП",
            value=org.requisites.unp if org else "",
            hint="9 цифр",
            keyboard_type=ft.KeyboardType.NUMBER,
            max_len=9,
        )

        self.unp.on_change = lambda e: self.on_change_handler(
            self.unp, OrgValidator.validate_unp
        )

        self.address = AppTextField(
            label="Адрес",
            value=org.requisites.address if org else "",
            hint="г. Минск, ул. Центральная, д. 1",
        )

        self.address.on_change = lambda e: self.on_change_handler(
            self.address, OrgValidator.validate_address
        )

        self.bank_account = AppTextField(
            label="Расчетный счет (IBAN)",
            value=org.requisites.bank_account if org else "",
            hint="BY20XXXX...",
            max_len=28,
        )

        self.bank_account.on_change = lambda e: self.on_change_handler(
            self.bank_account, OrgValidator.validate_bank_account
        )

        self.name_of_bank = AppTextField(
            label="Название банка",
            value=org.requisites.name_of_bank if org else "",
            hint="ОАО 'Приорбанк'",
        )

        self.name_of_bank.on_change = lambda e: self.on_change_handler(
            self.name_of_bank, OrgValidator.validate_name_of_bank
        )

        self.bic = AppTextField(
            label="БИК банка",
            value=org.requisites.bic if org else "",
            hint="8 символов",
            max_len=8,
        )

        self.bic.on_change = lambda e: self.on_change_handler(
            self.bic, OrgValidator.validate_bic
        )

        self.mobile_num = AppTextField(
            label="Моб. номер",
            value=org.requisites.mobile_num if org else "",
            hint="+375...",
            is_numer=True,
        )

        self.mobile_num.on_change = lambda e: self.on_change_handler(
            self.mobile_num, OrgValidator.validate_mobile_num
        )

        self.e_mail = AppTextField(
            label="E-mail",
            value=org.requisites.e_mail if org else "",
            hint="example@mail.com",
        )

        self.e_mail.on_change = lambda e: self.on_change_handler(
            self.e_mail, OrgValidator.validate_e_mail
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
            self.save_btn,
            ft.TextButton("Назад", on_click=self.close_dialog),
        ]

    def on_change_handler(self, field, validator):
        try:
            validator(field.value)
            field.error = None
        except ValidationError as err:
            field.error = str(err)

        self.update_save_state()
        self.page.update()

    def update_save_state(self):
        self.form_fields = [
            self.name,
            self.manager_name,
            self.agreement,
            self.fee,
            self.act_counter,
            self.date_field,
            self.unp,
            self.address,
            self.bank_account,
            self.name_of_bank,
            self.bic,
            self.mobile_num,
            self.e_mail,
        ]
        self.save_btn.disabled = any(field.error for field in self.form_fields)

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

    def close_dialog(self, e):
        self.open = False
        self.page.update()

    def save_data(self, e):
        try:
            raw_data = self.collect_raw_data()

            obj = OrgServices.build_org(raw_data)
            self.callback_on_save(obj)
            self.close_dialog(e)

        except Exception as ex:
            self.page.show_dialog(ft.SnackBar(ft.Text(f"Ошибка {ex}")))
