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
                            ft.DataCell(ft.Text(str(value), max_lines=5, overflow=ft.TextOverflow.ELLIPSIS))
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

        def on_nav_change(e):
            selected_index = e.control.selected_index
            if selected_index == 0:
                self.page.go("/introduction")
            elif selected_index == 1:
                self.page.go("/user/user-list")
            elif selected_index == 2:
                self.page.go("/user/user-statistics")

        navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.INFO, label="소개"),
                ft.NavigationDestination(icon=ft.icons.PEOPLE, label="사용자목록"),
                ft.NavigationDestination(icon=ft.icons.BAR_CHART, label="사용자 통계"),
            ],
            on_change=on_nav_change,
            selected_index=0  # 현재 선택된 메뉴 인덱스
        )

        self.controls = [
            ft.AppBar(title=ft.Text("Home"), bgcolor=ft.colors.AMBER_100),
            ft.Column(
                [
                    ft.Column(
                        [
                            ft.Text(f"{email}님 환영합니다!", size=30),
                            user_table,
                            ft.ElevatedButton("로그아웃", on_click=logout),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True
                    ),
                    navigation_bar
                ],
                expand=True
            )
        ]

class IntroductionView(ft.View):
    def __init__(self, page, auth):
        super().__init__()
        self.page = page
        self.auth = auth
        self.build()

    def build(self):
        def on_nav_change(e):
            selected_index = e.control.selected_index
            if selected_index == 0:
                self.page.go("/introduction")
            elif selected_index == 1:
                self.page.go("/user/user-list")
            elif selected_index == 2:
                self.page.go("/user/user-statistics")

        def logout(e):
            self.page.session.remove("user")
            self.page.go("/user/login")

        navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.INFO, label="소개"),
                ft.NavigationDestination(icon=ft.icons.PEOPLE, label="사용자목록"),
                ft.NavigationDestination(icon=ft.icons.BAR_CHART, label="사용자 통계"),
            ],
            on_change=on_nav_change,
            selected_index=0
        )

        self.controls = [
            ft.AppBar(title=ft.Text("소개"), bgcolor=ft.colors.AMBER_100),
            ft.Column(
                [
                    ft.Text("여기는 소개 페이지입니다.", size=30),
                    ft.ElevatedButton('로그아웃', on_click=logout)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            ),
            navigation_bar
        ]

class UserListView(ft.View):
    def __init__(self, page, auth):
        super().__init__()
        self.page = page
        self.auth = auth
        self.build()

    def build(self):
        def on_nav_change(e):
            selected_index = e.control.selected_index
            if selected_index == 0:
                self.page.go("/introduction")
            elif selected_index == 1:
                self.page.go("/user/user-list")
            elif selected_index == 2:
                self.page.go("/user/user-statistics")

        navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.INFO, label="소개"),
                ft.NavigationDestination(icon=ft.icons.PEOPLE, label="사용자목록"),
                ft.NavigationDestination(icon=ft.icons.BAR_CHART, label="사용자 통계"),
            ],
            on_change=on_nav_change,
            selected_index=1
        )

        # 사용자 목록 예시
        user_list = [
            ft.Text("사용자 1"),
            ft.Text("사용자 2"),
            ft.Text("사용자 3"),
        ]

        self.controls = [
            ft.AppBar(title=ft.Text("사용자목록"), bgcolor=ft.colors.AMBER_100),
            ft.Column(
                user_list,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            ),
            navigation_bar
        ]

class UserStatisticsView(ft.View):
    def __init__(self, page, auth):
        super().__init__()
        self.page = page
        self.auth = auth
        self.build()

    def build(self):
        def on_nav_change(e):
            selected_index = e.control.selected_index
            if selected_index == 0:
                self.page.go("/introduction")
            elif selected_index == 1:
                self.page.go("/user/user-list")
            elif selected_index == 2:
                self.page.go("/user/user-statistics")

        navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.INFO, label="소개"),
                ft.NavigationDestination(icon=ft.icons.PEOPLE, label="사용자목록"),
                ft.NavigationDestination(icon=ft.icons.BAR_CHART, label="사용자 통계"),
            ],
            on_change=on_nav_change,
            selected_index=2
        )

        # 사용자 통계 예시
        statistics = [
            ft.Text("총 사용자 수: 100"),
            ft.Text("활성 사용자 수: 80"),
            ft.Text("비활성 사용자 수: 20"),
        ]

        self.controls = [
            ft.AppBar(title=ft.Text("사용자 통계"), bgcolor=ft.colors.AMBER_100),
            ft.Column(
                statistics,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            ),
            navigation_bar
        ]
