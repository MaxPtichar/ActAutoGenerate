import flet as ft


class AppTextField(ft.TextField):
    def __init__(
        self,
        label: str,
        hint: str = "",
        tooltip: str = None,
        is_numer: bool = False,
        max_len: int = None,
        multiline: bool = False,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.label = label
        self.hint_text = hint
        self.tooltip = tooltip
        self.counter_text = " "
        self.max_length = max_len
        self.multiline = multiline

        # design
        self.border_width = 1.6
        self.border_radius = 6
        self.border_color = ft.Colors.BLUE_GREY_200
        self.focused_border_color = ft.Colors.BLUE_700
        self.focused_border_width = 2

        # text color
        self.label_style = ft.TextStyle(
            color=ft.Colors.BLUE_GREY_200, weight=ft.FontWeight.W_500
        )
        self.selection_color = ft.Colors.BLUE_100

        # padding
        self.content_padding = ft.padding.all(15)
        self.text_size = 14

        if is_numer:
            self.keyboard_type = ft.KeyboardType.NUMBER

        self.capitalization = ft.TextCapitalization.SENTENCES
