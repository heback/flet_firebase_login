import flet as ft

class LoginView(ft.View):
    def __init__(self, page, auth):
        super().__init__()
        self.page = page
        self.auth = auth
        self.build()

    def build(self):

        email = ft.TextField(label="Email", width=300)
        password = ft.TextField(label="Password", password=True, width=300)
        message = ft.Text()

        def login(e):
            try:
                user = self.auth.sign_in_with_email_and_password(email.value, password.value)
                self.page.session.set("user", user)
                self.page.go("/home")
            except Exception as e:
                message.value = f"오류: {str(e)}"
                self.update()

        self.controls = [
            ft.AppBar(title=ft.Text("Login"), bgcolor=ft.colors.TEAL_100),
            ft.Column(
                [
                    ft.Text("로그인", size=30),
                    email,
                    password,
                    ft.ElevatedButton("로그인", on_click=login),
                    ft.TextButton("회원가입", on_click=lambda e: self.page.go("/user/signup")),
                    ft.TextButton("비밀번호 재설정", on_click=lambda e: self.page.go("/user/reset-password")),
                    message,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]
