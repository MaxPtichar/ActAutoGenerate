import flet as ft

from src.UI.views.main_view import build_app


def main(page: ft.Page):
    build_app(page)


if __name__ == "__main__":
    ft.app(target=main)
