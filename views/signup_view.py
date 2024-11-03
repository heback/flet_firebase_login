import flet as ft

class SignupView(ft.View):
    def __init__(self, page, auth):
        super().__init__()
        self.page = page
        self.auth = auth
        self.build()

    def build(self):
        email = ft.TextField(label="Email", width=300)
        password = ft.TextField(label="Password", password=True, width=300)
        confirm_password = ft.TextField(label="Confirm Password", password=True, width=300)
        message = ft.Text()

        def signup(e):
            if password.value != confirm_password.value:
                message.value = "비밀번호가 일치하지 않습니다."
                self.update()
                return
            try:
                self.auth.create_user_with_email_and_password(email.value, password.value)
                message.value = "회원가입 성공!"
                self.page.go("/")
            except Exception as e:
                message.value = f"오류: {str(e)}"
            self.update()

        self.controls = [
            ft.Column(
                [
                    ft.Text("회원가입", size=30),
                    email,
                    password,
                    confirm_password,
                    ft.ElevatedButton("회원가입", on_click=signup),
                    ft.TextButton("로그인으로 돌아가기", on_click=lambda e: self.page.go("/")),
                    message,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]
