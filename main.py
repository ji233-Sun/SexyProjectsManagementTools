import flet as ft
from controllers.HomePage import HomePageController


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
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        HomePageController.HomePageController()
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)