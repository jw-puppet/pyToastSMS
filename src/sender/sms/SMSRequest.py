from typing import List
from src import rest_wrap


class SMSRequest(object):
    """
    SMS Request 객체
    full doc here (https://docs.toast.com/ko/Notification/SMS/ko/api-guide-v2.0/#sms_1)
    """
    def __init__(self, send_no: str, recipient_list: List[dict], body: str, **kwargs):
        super(SMSRequest, self).__init__()

        # Required
        self.sendNo: str = send_no
        self.recipientList: List[dict] = recipient_list
        self.body: str = body

        # Optional
        self.templateId: str = None
        self.requestDate: str = None
        self.userId: str = None

        for k in kwargs.keys():
            if k in self.__dict__.keys():
                print(str(k) + " set.")
                self.__setattr__(k, kwargs.get(k))

    def to_dict(self) -> dict:
        dict_body = {k: v for k, v in self.__dict__.items() if v is not None}
        return dict_body

    @rest_wrap
    def send_sms(self):
        return self.to_dict()
