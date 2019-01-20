from typing import List

import enforce

from config import secret
from src import sender
from src.sender.mms import MMS
from src.sender.sms import SMS


class ToastSMSManager(object):
    """
    PyToastSms
    """
    _appKey = secret.get('app_key')

    @enforce.runtime_validation
    def __init__(self, app_key: str = None):
        super(ToastSMSManager, self).__init__()
        self._appKey: str = app_key or self._appKey

    @enforce.runtime_validation
    def send_sms(self, send_no: str, recipient_list: List[dict], body: str, **kwargs):
        return SMS.Request(send_no, recipient_list, body, **kwargs).send_sms()

    @enforce.runtime_validation
    def send_mms(self, send_no: str, recipient_list: List[dict], title: str, body: str, **kwargs):
        return MMS.Request(send_no, recipient_list, title, body, **kwargs).send_mms()

    @classmethod
    def list_send_nos(cls):
        return sender.list_send_nos()

    @classmethod
    def list_sent_sms(cls, requestId: str = None, startRequestDate: str = None, endRequestDate: str = None):
        return SMS.list_sent_sms(requestId, startRequestDate, endRequestDate)
