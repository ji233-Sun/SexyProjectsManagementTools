import flet as ft
from flet.core.file_picker import FilePickerResultEvent, FilePicker

class ProjectBoxController(ft.Row):
    def __init__(self, project_name, project_folder, ori_page):
        super().__init__()
        self.project_folder = project_folder
        self.ori_page = ori_page

        def get_directory_result(e: FilePickerResultEvent):
            self.project_folder = e.path if e.path else "Cancelled!"

        self.get_directory_dialog = FilePicker(on_result=get_directory_result)

        self.project_name = ft.Text(project_name)
        self.project_name_editor = ft.TextField(label="New Name",value=self.project_name.value, visible=False)
        self.project_name_edit_confirm_button = ft.FloatingActionButton(icon=ft.Icons.CHECK, on_click=self.edit_name_confirm, visible=False)
        self.enter_project_button = ft.TextButton(icon=ft.Icons.TRANSIT_ENTEREXIT, text="Enter Project", on_click=self.enter_project_click)
        self.edit_project_name_button = ft.TextButton(icon=ft.Icons.EDIT, text="Edit Project Name", on_click=self.edit_name_click)
        self.delete_project_button = ft.TextButton(icon=ft.Icons.DELETE, text="Delete Project", on_click=self.delete_project_click)
        self.controls = [
            self.get_directory_dialog,
            self.project_name,
            self.project_name_editor,
            self.project_name_edit_confirm_button,
            self.enter_project_button,
            self.edit_project_name_button,
            self.delete_project_button,
        ]


    def edit_name_click(self, e):
        self.project_name.visible = False
        self.project_name_edit_confirm_button.visible = True
        self.project_name_editor.value = ""
        self.project_name_editor.visible = True
        self.update()

    def edit_name_confirm(self, e):
        self.project_name.value = self.project_name_editor.value
        self.project_name.visible = True
        self.project_name_edit_confirm_button.visible = False
        self.project_name_editor.value = ""
        self.project_name_editor.visible = False
        self.update()

    def delete_project_click(self, e):
        self.parent.controls.remove(self)
        self.parent.update()

    def enter_project_click(self, e):
        self.ori_page.go("/project")