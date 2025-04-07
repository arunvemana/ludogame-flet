import flet as ft

def main(page: ft.Page):
    page.title = "Ludo Board (6x6 homes)"
    board = []

    # Arrow/special tiles (positions may need tuning)
    arrows = {
        (6, 1): "⬆️", (6, 13): "⬇️",
        (1, 8): "➡️", (13, 6): "⬅️",
        (2, 2): "⭐", (2, 12): "⭐", (12, 2): "⭐", (12, 12): "⭐",
    }

    def get_cell(row, col):
        color = ft.Colors.WHITE
        icon = None

        # Central star (final destination)
        if (row, col) == (7, 7):
            color = ft.Colors.GREY_900

        # White cross path (vertical and horizontal)
        elif row in [6, 7, 8] or col in [6, 7, 8]:
            color = ft.Colors.WHITE

        # Red home (top-left 6x6)
        elif row < 6 and col < 6:
            color = ft.Colors.RED_300

        # Green home (top-right 6x6)
        elif row < 6 and col > 8:
            color = ft.Colors.GREEN_300

        # Blue home (bottom-left 6x6)
        elif row > 8 and col < 6:
            color = ft.Colors.BLUE_300

        # Yellow home (bottom-right 6x6)
        elif row > 8 and col > 8:
            color = ft.Colors.YELLOW_300

        # Safe/star tiles
        if (row, col) in arrows:
            icon = arrows[(row, col)]

        return ft.Container(
            width=35,
            height=35,
            bgcolor=color,
            alignment=ft.alignment.center,
            border=ft.border.all(0, ft.Colors.BLACK),
            content=ft.Column([ft.Text(icon or "", size=20)]),padding=0,margin=0
        )

    for row in range(15):
        row_cells = []
        for col in range(15):
            row_cells.append(get_cell(row, col))
        board.append(ft.Row(row_cells, spacing=0,run_spacing=0))


    page.add(*board)

ft.app(target=main)
