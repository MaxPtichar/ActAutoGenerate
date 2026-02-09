import flet as ft

from src.UI.views.main_view import build_app


async def main(page: ft.Page):
    await build_app(page)


if __name__ == "__main__":
    ft.app(target=main)
