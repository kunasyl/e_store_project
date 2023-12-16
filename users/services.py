from typing import Protocol, OrderedDict

from rest_framework_simplejwt import tokens

from . import repos


class UserServicesInterface(Protocol):

    def create_user(self, data: OrderedDict) -> None: ...

    def create_token(self, data: OrderedDict) -> dict: ...

    def create_cart(self, data: OrderedDict) -> None: ...


class UserServicesV1:
    user_repos: repos.UserReposInterface = repos.UserReposV1()

    def create_user(self, data: OrderedDict) -> None:
        user = self.user_repos.create_user(data=data)
        if user:
            self.create_cart(user)
        self._send_letter_to_email(email=user.email)

    def create_cart(self, user_id) -> None:
        self.user_repos.create_cart(user_id=user_id)

    @staticmethod
    def _send_letter_to_email(email: str) -> None:
        print(f'send letter to {email}')

    def create_token(self, data: OrderedDict) -> dict:
        user = self.user_repos.get_user(data=data)

        access = tokens.AccessToken.for_user(user=user)
        refresh = tokens.RefreshToken.for_user(user=user)

        return {
            'access': str(access),
            'refresh': str(refresh),
        }
