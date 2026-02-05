from turtle import onclick

import flet as ft

import doc_engine


def main(page: ft.Page):
    page.title = "Генератор актов"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(ft.ElevatedButton("Создать акт", on_click=doc_engine.create_files))


ft.run(main)
