import pyrebase
from flet import *
import datetime
from functools import partial

# firebase project config info
config = {
    "apiKey": "AIzaSyDhCADzL0Pu6ljILrAiVckNs3BmXJqb-pU",
    "authDomain": "flet-firebase-ced4d.firebaseapp.com",
    "projectId": "flet-firebase-ced4d",
    "storageBucket": "flet-firebase-ced4d.appspot.com",
    "messagingSenderId": "570468785109",
    "appId": "1:570468785109:web:008672c9c6e4e233007b5c",
    "databaseURL": ""
};

# initialize firebase
firebase = pyrebase.initialize_app(config)

# set up authentication manager
auth = firebase.auth()


# UI class
class UserWidget(UserControl):
    def __init__(
            self,
            title: str,
            sub_title: str,
            btn_name: str,
            func
    ):
        self.title = title
        self.sub_title = sub_title
        self.btn_name = btn_name
        self.func = func
        super().__init__()

    def InputTextField(self, text:str, hide:bool):
        return Container(
            alignment=alignment.center,
            content=TextField(
                height=48,
                width=255,
                bgcolor='#f0f3f6',
                text_size=12,
                color='black',
                border_color='transparent',
                hint_text=text,
                filled=True,
                cursor_color='black',
                hint_style=TextStyle(
                    size=11,
                    color='black'
                ),
                password=hide
            )
        )

    def SignInOption(self, path: str, name: str):
        return Container(
            content=ElevatedButton(
                content=Row(
                    alignment='center',
                    spacing=4,
                    controls=[
                        Image(
                            src=path,
                            width=30,
                            height=30,
                        ),
                        Text(
                            name,
                            color='black',
                            size=10,
                            weight='bold'
                        )
                    ]
                ),
                style=ButtonStyle(
                    shape={
                        '': RoundedRectangleBorder(radius=8),
                    },
                    bgcolor={
                        '': '#f0f3f6',
                    }
                )
            )
        )

    def build(self):

        self._title = Container(
            alignment=alignment.center,
            content=Text(
                self.title,
                size=15,
                text_align='center',
                weight='bold',
                color='black'
            )
        )

        self._sub_title = Container(
            alignment=alignment.center,
            content=Text(
                self.sub_title,
                size=10,
                text_align='center',
                color='black'
            )
        )

        self._sign_in = Container(
            content=ElevatedButton(
                on_click=self.func,
                content=Text(
                    self.btn_name,
                    size=11,
                    weight='bold'
                ),
                style=ButtonStyle(
                    shape={
                        '': RoundedRectangleBorder(radius=8)
                    },
                    color={
                        '': 'white',
                    },
                    bgcolor={
                        '': 'black'
                    }
                ),
                height=48,
                width=255

            )
        )
        return Column(
            horizontal_alignment='center',
            controls=[
                Container(padding=10),
                self._title,
                self._sub_title,
                Column(
                    spacing=12,
                    controls=[
                        self.InputTextField('Email', False),
                        self.InputTextField('Password', True)
                    ]
                ),
                Container(padding=5),
                self._sign_in,
                Container(padding=5),
                Column(
                    horizontal_alignment='centr',
                    controls=[
                        Container(
                            content=Text(
                                'Or continue with',
                                size=10,
                                color='black',
                            )
                        ),
                        self.SignInOption(f'facebook.png', 'Facebook'),
                        self.SignInOption(f'google.png', 'Google'),
                    ]
                )

            ]

        )


def main(page: Page):
    page.title = "Flet with firebase"
    page.bgcolor = "#f0f3f6"
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    def _main_column():
        return Container(
            width=280,
            height=600,
            bgcolor='#ffffff',
            padding=12,
            border_radius=35,
            content=Column(
                spacing=20,
                horizontal_alignment='center'
            )
        )

    def _register_user(e):
        try:
            auth.create_user_with_email_and_password(
                _register_.controls[0].controls[3].controls[0].content.value,
                _register_.controls[0].controls[3].controls[1].content.value,
            )
            print('Registration OK!')

        except Exception as e:
            print(e)

    def _sign_in(e):
        try:
            user = auth.sign_in_with_email_and_password(
                _sign_in_.controls[0].controls[3].controls[0].content.value,
                _sign_in_.controls[0].controls[3].controls[1].content.value,
            )

            info = auth.get_account_info(user['idToken'])
            print(info)

            data = ['createdAt', 'lastLoginAt']

            for key in info:
                if key == 'users':
                    for item in data:
                        print(
                            item
                            + ' '
                            + datetime.datetime.fromtimestamp(
                                int(info[key][0][item]) / 1000
                            ).strftime('%D - %H:%M %p')
                        )

            _sign_in_.controls[0].controls[3].controls[0].content.value = None
            _sign_in_.controls[0].controls[3].controls[1].content.value = None
            _sign_in_.controls[0].controls[3].update()

        except Exception as e:
            print('Wrong email or password')

    _sign_in_ = UserWidget(
        'Welcome back!',
        'Enter your account details below.',
        'Sign In',
        _sign_in
    )

    _register_ = UserWidget(
        'Registration',
        'Register your email and password below.',
        'Register',
        _register_user
    )

    _sign_in_main = _main_column()
    _sign_in_main.content.controls.append(Container(padding=15))
    _sign_in_main.content.controls.append(_sign_in_)

    _reg_main = _main_column()
    _reg_main.content.controls.append(Container(padding=15))
    _reg_main.content.controls.append(_register_)

    page.add(
        Row(
            alignment='center',
            spacing=25,
            controls=[
                _sign_in_main,
                _reg_main
            ]
        )
    )


if __name__ == '__main__':
    flet.app(target=main, assets_dir='assets')
