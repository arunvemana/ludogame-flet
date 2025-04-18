import os.path
from idlelib.browser import transform_children

import flet as ft

def main(page: ft.Page):
    page.title = "Ludo Board (6x6 homes)"
    # page.window_width = 500  # Set the desired width
    # page.window_height = 1000  # Set the desired height
    board = []

    # Arrow/special tiles (positions may need tuning)
    # arrows = {
    #     (6, 5): "⬆️", (0, 7): "⬇️",
    #     (7, 0): "", (13, 6): "⬅️",
    #     (2, 2): "⭐", (2, 12): "⭐", (12, 2): "⭐", (12, 12): "⭐",
    # }

    arrows = {
        (7,0) :"./resources/icons/right_arrow.png",
        (0,7):"./resources/icons/down_arrow.png",
        (7,14):"./resources/icons/left_arrow.png",
        (14,7):"./resources/icons/top_arrow.png"
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
            icon = ft.Image(src=os.path.abspath(arrows[(row,col)]),width=30, height=30)
            print(icon)

        return ft.Container(
            width=40,  # Cell size
            height=40,  # Cell size
            bgcolor=color,
            alignment=ft.alignment.center,
            border=ft.border.all(1, ft.Colors.BLACK),  # Added border
            content=ft.Column([icon or ft.Text("", size=20,color=ft.Colors.BLUE)]), padding=0, margin=0  # No padding/margin
        )

    for row in range(15):
        row_cells = []
        for col in range(15):
            row_cells.append(get_cell(row, col))
        # Use ft.Row with spacing set to 0
        board.append(ft.Row(row_cells, spacing=0, run_spacing=0,alignment=ft.MainAxisAlignment.CENTER))
    page.update()
#
#     # Use ft.Column to stack rows without gaps
    page.add(ft.Column(board, spacing=0, run_spacing=0))
#
# page.update()

ft.app(target=main)