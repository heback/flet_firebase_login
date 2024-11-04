import flet as ft

class HomeView(ft.View):
    def __init__(self, page, auth):
        super().__init__()
        self.page = page
        self.auth = auth
        self.build()

    def build(self):
        user = self.page.session.get("user")
        email = user['email'] if user else "Unknown"

        def logout(e):
            self.page.session.remove("user")
            self.page.go("/")

        self.controls = [
            ft.AppBar(title=ft.Text("Home"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Column(
                [
                    ft.Text(f"{email}님 환영합니다!", size=30),
                    ft.ElevatedButton("로그아웃", on_click=logout),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]
