from typing import NoReturn

from .interface.i_member_service import IMemberService


class MemberService(IMemberService):

    def save(self) -> NoReturn:
        print('save method callable!!')
