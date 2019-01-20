from src import rest_wrap
from src.sender.sms.SMSRequest import SMSRequest


class SMS(object):
    Request = SMSRequest

    @classmethod
    @rest_wrap
    def list_sent_sms(cls, requestId: str = None, startRequestDate: str = None, endRequestDate: str = None):
        assert not (requestId == startRequestDate == endRequestDate is None)

        return {k: v for k, v in dict(
            requestId=requestId,
            startRequestDate=startRequestDate,
            endRequestDate=endRequestDate).items()
                if v is not None}
