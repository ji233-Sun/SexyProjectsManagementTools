import flet as ft

from Controller.HomePage.ProjectBoxController import ProjectBoxController


class HomePageController(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
            ft.FloatingActionButton(
                icon=ft.Icons.ADD,
                on_click=self.add_button_on_click
            )
        ]

    def add_button_on_click(self, e):
        self.controls.append(ProjectBoxController("New Project", ""))
        self.update()

