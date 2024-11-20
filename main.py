import flet as ft
import pyrebase

from views.signup_view import SignupView
from views.login_view import LoginView
from views.reset_password_view import ResetPasswordView
from views.home_view2 import HomeView, IntroductionView, UserListView, UserStatisticsView

# Firebase 설정
# 자신의 설정으로 교체
firebaseConfig = {
  'apiKey': "AIzaSyA8gTf61ob6mBMY9Tqje16vcitYpsXIOGw",
  'authDomain': "flet-course.firebaseapp.com",
  'databaseURL': "https://flet-course-default-rtdb.firebaseio.com",
  'projectId': "flet-course",
  'storageBucket': "flet-course.appspot.com",
  'messagingSenderId': "663795272566",
  'appId': "1:663795272566:web:b8fa9d387ad837cc1e8857"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 800
    page.window.resizable = False
    page.title = "Firebase Auth with Flet"
    # 초기 화면 설정
    page.views.append(LoginView(page, auth))
    page.route = '/user/login'

    def route_change(e):
        page.views.clear()
        if page.route == "/user/login":
            page.views.append(LoginView(page, auth))
        elif page.route == "/user/signup":
            page.views.append(SignupView(page, auth))
        elif page.route == "/user/reset-password":
            page.views.append(ResetPasswordView(page, auth))
        elif page.route == "/user/user-list":
            page.views.append(UserListView(page, auth))
        elif page.route == "/user/user-statistics":
            page.views.append(UserStatisticsView(page, auth))
        elif page.route == "/home":
            page.views.append(HomeView(page, auth))
        elif page.route == "/introduction":
            page.views.append(IntroductionView(page, auth))
        page.update()

    # def view_pop(view):
    #     page.views.pop()
    #     top_view = page.views[-1]
    #     page.go(top_view.route)

    page.on_route_change = route_change
    # page.on_view_change = view_pop
    page.go(page.route)

ft.app(target=main)
