import flet as ft
import pyrebase

from views.signup_view import SignupView
from views.login_view import LoginView
from views.reset_password_view import ResetPasswordView
from views.home_view import HomeView

# Firebase 설정
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
    page.title = "Firebase Auth with Flet"
    # 초기 화면 설정
    page.views.append(LoginView(page, auth))

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth))
        elif page.route == "/signup":
            page.views.append(SignupView(page, auth))
        elif page.route == "/reset-password":
            page.views.append(ResetPasswordView(page, auth))
        elif page.route == "/home":
            page.views.append(HomeView(page, auth))
        page.update()

    # def view_pop(view):
    #     page.views.pop()
    #     top_view = page.views[-1]
    #     page.go(top_view.route)

    page.on_route_change = route_change
    # page.on_view_change = view_pop
    page.go(page.route)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
