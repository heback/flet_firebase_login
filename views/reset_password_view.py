import flet as ft

class ResetPasswordView(ft.View):
    def __init__(self, page, auth):
        super().__init__()
        self.page = page
        self.auth = auth
        self.build()

    def build(self):
        email = ft.TextField(label="Email", width=300)
        message = ft.Text()

        def reset_password(e):
            try:
                self.auth.send_password_reset_email(email.value)
                message.value = "비밀번호 재설정 이메일을 보냈습니다."
            except Exception as e:
                message.value = f"오류: {str(e)}"
            self.update()

        self.controls = [
            ft.AppBar(title=ft.Text("Password Reset"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Column(
                [
                    ft.Text("비밀번호 재설정", size=30),
                    email,
                    ft.ElevatedButton("재설정 링크 보내기", on_click=reset_password),
                    ft.TextButton("로그인으로 돌아가기", on_click=lambda e: self.page.go("/user/login")),
                    message,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]
