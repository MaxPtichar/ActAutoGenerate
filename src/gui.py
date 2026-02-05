from turtle import onclick

import flet as ft

import doc_engine


def main(page: ft.Page):
    page.title = "Генератор актов"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(ft.Button("Создать акты", on_click=doc_engine.create_files))

    # Поля для основной информации об организации
    name = ft.TextField(label="Название организации", hint_text="ООО 'ПримерТехно'")
    manager_name = ft.TextField(
        label="Имя руководителя", hint_text="Иванов Иван Иванович"
    )
    agreement = ft.TextField(label="Договор", hint_text="№ 123-А от 01.01.2026")
    fee = ft.TextField(
        label="Стоимость услуг",
        hint_text="500.00",
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    act_counter = ft.TextField(
        label="Номер акта",
        value="1",
        tooltip="Отсчет актов начнется с введенного номера",
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    # Реквизиты (Requisites)
    unp = ft.TextField(
        label="УНП", hint_text="9 цифр", keyboard_type=ft.KeyboardType.NUMBER
    )
    address = ft.TextField(label="Адрес", hint_text="г. Минск, ул. Центральная, д. 1")
    bank_account = ft.TextField(label="Расчетный счет (IBAN)", hint_text="BY20XXXX...")
    name_of_bank = ft.TextField(label="Название банка", hint_text="ОАО 'Приорбанк'")
    bic = ft.TextField(label="БИК банка", hint_text="8-11 символов")
    mobile_num = ft.TextField(
        label="Моб. номер", hint_text="+375...", keyboard_type=ft.KeyboardType.PHONE
    )
    e_mail = ft.TextField(label="E-mail", hint_text="example@mail.com")

    # Собираем всё в колонку для AlertDialog
    org_column = ft.Column(
        controls=[
            ft.Text("Основные данные", weight="bold"),
            name,
            manager_name,
            agreement,
            fee,
            act_counter,
        ]
    )

    req_column = ft.Column(
        controls=[
            ft.Text("Реквизиты и контакты", weight="bold"),
            unp,
            address,
            bank_account,
            name_of_bank,
            bic,
            mobile_num,
            e_mail,
        ]
    )

    dialog_content = ft.Row(controls=[org_column, req_column])
    #     tight=True,
    #     scroll=ft.ScrollMode.ALWAYS, # Добавляем прокрутку, так как полей много
    #     height=400 # Ограничиваем высоту, чтобы окно не вылетало за экран
    # )
    dialog_alert = ft.AlertDialog(title="Новая организация", content=dialog_content)

    page.add(
        ft.Button(
            "Добавить организацию", on_click=lambda e: page.show_dialog(dialog_alert)
        )
    )
    # unp: str
    # address: str
    # bank_account: str
    # name_of_bank: str
    # bic: str
    # mobile_num: str
    # e_mail: str

    # id: int
    # name:
    # manager_name: str
    # agreement: str
    # fee: float
    # act_counter: int
    # date: date
    # requisites: Requisites
    # last_issued_num: int = 0


ft.run(main)
