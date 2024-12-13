import flet as ft
from controllers.HomePage import HomePageController
from controllers.ProjectManagePage.ProjectManagePageController import ProjectManagePageController


def main(page: ft.Page):
    page.title = "Sexy Projects Management utils"

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(
                            title=ft.Text("Home"),
                            bgcolor=ft.Colors.GREY_900,
                        ),
                        HomePageController.HomePageController(page)
                    ],
                )
            )
        if page.route == "/project":
            page.views.append(
                ft.View(
                    "/project",
                    [
                        ft.AppBar(
                            title=ft.Text("Project"),
                            bgcolor=ft.Colors.GREY_900,
                            leading=ft.IconButton(
                                ft.Icons.HOME,
                                on_click=lambda _: page.go("/"),
                            ),
                        ),
                        ProjectManagePageController(page)
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.views.clear()
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)