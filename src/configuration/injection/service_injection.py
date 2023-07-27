from inject import Binder

from service.member_service import IMemberService, MemberService


def service_injection(binder: Binder):
    binder.bind_to_constructor(IMemberService, MemberService)
