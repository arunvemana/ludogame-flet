import os
import flet as ft
import flet.canvas as cv

# Define the home areas as before
green_box = [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (1, 8)]
red_box = [(6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)]
blue_box = [(13, 6), (13, 7), (12, 7), (11, 7), (10, 7), (9, 7), (8, 7)]
yellow_box = [(8, 13), (7, 13), (7, 12), (7, 11), (7, 10), (7, 9), (7, 8)]

def main(page: ft.Page):
    page.title = "Ludo Board with Triangular Home Areas"

    # Size of each cell
    cell_size = 40

    arrows = {
        (7, 0): "./resources/icons/right_arrow.png",
        (0, 7): "./resources/icons/down_arrow.png",
        (7, 14): "./resources/icons/left_arrow.png",
        (14, 7): "./resources/icons/top_arrow.png"
    }

    def is_home_area(row, col):
        return (
            (0 <= row < 6 and 0 <= col < 6) or  # Red
            (0 <= row < 6 and 9 <= col < 15) or  # Green
            (9 <= row < 15 and 0 <= col < 6) or  # Blue
            (9 <= row < 15 and 9 <= col < 15)  # Yellow
        )

    def get_cell(row, col):
        color = ft.Colors.WHITE
        icon = None

        # Central star (final destination)
        if (row, col) == (7, 7):
            color = ft.Colors.GREY_900

        # Assign colors based on the home boxes
        if (row, col) in green_box:
            color = ft.Colors.GREEN
        elif (row, col) in red_box:
            color = ft.Colors.RED
        elif (row, col) in blue_box:
            color = ft.Colors.BLUE
        elif (row, col) in yellow_box:
            color = ft.Colors.YELLOW

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
            icon = ft.Image(src=os.path.abspath(arrows[(row, col)]), width=40, height=40,fit = ft.ImageFit.CONTAIN)

        return ft.Container(
            width=cell_size,
            height=cell_size,
            bgcolor=color,
            alignment=ft.alignment.bottom_right,
            border=None if is_home_area(row, col) else ft.border.all(0.5, ft.Colors.BLACK),
            # content=ft.Text(f"{row},{col}", size=8, color=ft.Colors.BLACK) if not icon else icon,
            padding=0,
            margin=0
        )

    # Create the board with cells
    board = []
    for row in range(15):
        row_cells = []
        for col in range(15):
            row_cells.append(get_cell(row, col))
        board.append(ft.Row(row_cells, spacing=0, run_spacing=0, alignment=ft.MainAxisAlignment.CENTER))

    # Create the canvas for the middle 9x9 area
    center = cv.Canvas(
        [
            # Red triangle (adjusted using printed coordinates)
            cv.Path(
                [
                    cv.Path.MoveTo(cell_size * 11 +3 , cell_size * 3),
                    cv.Path.LineTo(cell_size * 11 +3 , cell_size * 6),
                    cv.Path.LineTo(cell_size * 12.5, cell_size * 4.5),
                    cv.Path.Close(),
                ],
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.RED),
            ),

            # Green triangle (top-right)
            cv.Path(
                [   
                    cv.Path.MoveTo(cell_size * 11 +3 , cell_size * 3),
                    cv.Path.LineTo(cell_size * 14 + 2, cell_size * 3),
                    cv.Path.LineTo(cell_size * 12.5, cell_size * 4.5),
                    cv.Path.Close(),
                ],
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.GREEN),
            ),
            # Yellow triangle (bottom-right)
            cv.Path(
                [
                    cv.Path.MoveTo(cell_size * 14 +2, cell_size * 3),
                    cv.Path.LineTo(cell_size * 14 +2, cell_size * 6),
                    cv.Path.LineTo(cell_size * 12.5, cell_size * 4.5),
                    cv.Path.Close(),
                ],
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.YELLOW),
            ),
            # Blue triangle (bottom-left)
            cv.Path(
                [   
                    cv.Path.MoveTo(cell_size * 11 +2, cell_size * 6),
                    cv.Path.LineTo(cell_size * 14 +2, cell_size * 6),
                    cv.Path.LineTo(cell_size * 12.5, cell_size * 4.5),
                    cv.Path.Close(),
                ],
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.BLUE),
            ),
        ],
        width=cell_size * 9,
        height=cell_size * 9,
    )

    # Adjust the canvas to align with the central cells of the board
    center_container = ft.Container(
        center,
        width=cell_size * 9,
        height=cell_size * 9,
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=cell_size * 3, top=cell_size * 3),
    )

    # Create the canvas for the home circles
    home_circle_canvas = cv.Canvas(
        [
            # Red home circle
            cv.Circle(
                x = cell_size * 3,
                y = cell_size * 3,
                radius = cell_size * 3 - 2,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.WHITE),
            ),

            cv.Circle(
                x = cell_size * 12,
                y = cell_size * 3,
                radius = cell_size * 3 - 2,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.WHITE),
            ),

            cv.Circle(
                x = cell_size * 12,
                y = cell_size * 12,
                radius = cell_size * 3 - 2 ,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.WHITE),
            ),

            cv.Circle(
                x = cell_size * 3,
                y = cell_size * 12,
                radius = cell_size * 3 - 2,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.WHITE),
            ),

            # Red home tokens
            cv.Circle(
                x = cell_size * 2,
                y = cell_size * 2,
                radius= cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.RED),
            ),
            cv.Circle(
                x = cell_size * 4,
                y=  cell_size * 4,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.RED),
            ),
            cv.Circle(
                x = cell_size * 2,
                y = cell_size * 4,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.RED),
            ),
            cv.Circle(
                x = cell_size * 4,
                y = cell_size * 2,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.RED),
            ),

            # # Green home tokens
            cv.Circle(
                x = cell_size * 11,
                y = cell_size * 2,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.GREEN),
            ),
            cv.Circle(
                x = cell_size * 13,
                y = cell_size * 2,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.GREEN),
            ),
            cv.Circle(
                x = cell_size * 11,
                y = cell_size * 4,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.GREEN),
            ),
            cv.Circle(
                x = cell_size * 13,
                y = cell_size * 4,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.GREEN),
            ),

            # # Blue home tokens
            cv.Circle(
                x = cell_size * 2,
                y = cell_size * 11,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.BLUE),
            ),
            cv.Circle(
                x = cell_size * 4,
                y = cell_size * 11,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.BLUE),
            ),
            cv.Circle(
                x = cell_size * 2,
                y = cell_size * 13,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.BLUE),
            ),
            cv.Circle(
                x = cell_size * 4,
                y = cell_size * 13,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.BLUE),
            ),

            # # Yellow home tokens
            cv.Circle(
                x = cell_size * 11,
                y = cell_size * 11,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.YELLOW),
            ),
            cv.Circle(
                x = cell_size * 13,
                y = cell_size * 11,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.YELLOW),
            ),
            cv.Circle(
                x = cell_size * 11,
                y = cell_size * 13,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.YELLOW),
            ),
            cv.Circle(
                x = cell_size * 13,
                y = cell_size * 13,
                radius=cell_size * 0.5,
                paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.YELLOW),
            ),
           
        ],
        width=cell_size * 15,
        height=cell_size * 15,
    )

    # Add the home circle canvas to the page
    page.add(
        ft.Stack(
            [
                ft.Container(
                    ft.Column(board, spacing=0, run_spacing=0),
                    alignment=ft.alignment.center
                ),
                center_container,
                ft.Container(
                    home_circle_canvas,
                    alignment=ft.alignment.center
                )
            ]
        )
    )

ft.app(target=main)
