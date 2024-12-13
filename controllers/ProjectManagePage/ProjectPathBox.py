import flet as ft
from flet.core.file_picker import FilePicker, FilePickerResultEvent

from utils.openPath import open_folder


class ProjectPathBox(ft.Row):
    def __init__(self, path_name, path_value, ori_page):
        super().__init__()
        self.path_name = path_name
        self.path_value = path_value
        self.ori_page = ori_page

        def get_directory_result(e: FilePickerResultEvent):
            self.path_value = e.path if e.path else "Cancelled!"
            self.update()

        self.get_directory_dialog = FilePicker(on_result=get_directory_result)

        self.path_name = ft.Text(self.path_name)
        self.path_name_editor = ft.TextField(label="New Name", visible=False)
        self.path_name_edit_confirm_button = ft.FloatingActionButton(icon=ft.Icons.CHECK, on_click=self.edit_name_confirm, visible=False)
        self.path_open_button = ft.TextButton(icon=ft.Icons.FOLDER_OPEN, text="Open", on_click=self.open_path)
        self.path_choose_button = ft.TextButton(icon=ft.Icons.FOLDER, text="Choose", on_click=self.choose_path)
        self.path_name_edit_button = ft.TextButton(icon=ft.Icons.EDIT, text="Edit Name", on_click=self.edit_name)
        self.path_delete_button = ft.TextButton(icon=ft.Icons.DELETE, text="Delete", on_click=self.delete_path)
        self.controls = [
            self.get_directory_dialog,
            self.path_name,
            self.path_name_editor,
            self.path_name_edit_confirm_button,
            self.path_open_button,
            self.path_choose_button,
            self.path_name_edit_button,
            self.path_delete_button,
        ]

    def edit_name_confirm(self,e):
        self.path_name.value = self.path_name_editor.value
        self.path_name.visible = True
        self.path_name_edit_confirm_button.visible = False
        self.path_name_editor.value = ""
        self.path_name_editor.visible = False
        self.update()

    def open_path(self, e):
        open_folder(self.path_value)

    def choose_path(self, e):
        self.get_directory_dialog.get_directory_path()

    def edit_name(self, e):
        self.path_name.visible = False
        self.path_name_edit_confirm_button.visible = True
        self.path_name_editor.value = ""
        self.path_name_editor.visible = True
        self.update()

    def delete_path(self, e):
        self.parent.controls.remove(self)
        self.parent.update()