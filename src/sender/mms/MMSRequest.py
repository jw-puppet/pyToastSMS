from typing import List
from src import rest_wrap


class MMSRequest(object):
    """
    MMS Request 객체
    full doc here (https://docs.toast.com/ko/Notification/SMS/ko/api-guide-v2.0/#mms_1)
    """

    def __init__(self, send_no: str, recipient_list: List[dict], title: str, body: str, **kwargs):
        super(MMSRequest, self).__init__()

        # Required
        self.sendNo: str = send_no
        self.recipientList: List[dict] = recipient_list
        self.title: str = title
        self.body: str = body

        # Optional
        self.templateId: str = None
        self.requestDate: str = None
        self.userId: str = None

        for k in kwargs.keys():
            if k in self.__dict__.keys():
                self.__setattr__(k, kwargs.get(k))

    def to_dict(self) -> dict:
        dict_body = {k: v for k, v in self.__dict__.items() if v is not None}
        return dict_body

    @rest_wrap
    def send_mms(self):
        return self.to_dict()
