import flet
import flet as ft

from controllers.ProjectManagePage.ProjectPathBox import ProjectPathBox


class ProjectManagePageController(ft.Column):
    def __init__(self, ori_page):
        super().__init__()
        self.ori_page = ori_page
        self.ProjectName = "Test Project"
        self.ProjectPaths = {}

        self.add_path_button = ft.TextButton(
                icon=ft.Icons.ADD,
                text="Add Path",
                on_click=self.add_path_button_on_click
            )

        self.controls = [
            ft.Text(
                f"{self.ProjectName}",
                size=40,
                color=ft.Colors.WHITE,
                weight=ft.FontWeight.W_100,
            ),
            self.add_path_button
        ]


    def refresh_path_list(self):
        for key,value in self.ProjectPaths.items():
            self.controls.append(ProjectPathBox(key, value, self.ori_page))

        self.update()

    def add_path_button_on_click(self, e):
        self.ProjectPaths["New Path"] = "C:\\Users\\Administrator\\Desktop"
        self.refresh_path_list()
