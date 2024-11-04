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

        # 사용자 딕셔너리를 표로 변환
        if user:
            data_rows = []
            for key, value in user.items():
                data_rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(key))),
                            ft.DataCell(ft.Row(
                                controls=[
                                    ft.Text(
                                    str(value),
                                    max_lines=5,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                    )
                            ]))
                            # ft.DataCell(ft.Container(
                            #     content=ft.Text(
                            #         str(value),
                            #         max_lines=None,
                            #         overflow=ft.TextOverflow.VISIBLE,
                            #     ),
                            #     width=200,  # 셀의 너비를 설정하여 자동 개행 유도
                            # ))
                        ]
                    )
                )
            user_table = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("키")),
                    ft.DataColumn(ft.Text("값")),
                ],
                rows=data_rows,
            )
        else:
            user_table = ft.Text("사용자 데이터가 없습니다.")

        def logout(e):
            self.page.session.remove("user")
            self.page.go("/user/login")

        self.controls = [
            ft.AppBar(title=ft.Text("Home"), bgcolor=ft.colors.AMBER_100),
            ft.Column(
                [
                    ft.Text(f"{email}님 환영합니다!", size=30),
                    user_table,
                    ft.ElevatedButton("로그아웃", on_click=logout),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]
