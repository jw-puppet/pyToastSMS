from src import rest_wrap


@rest_wrap
def list_send_nos(use=True, block=False):
    """
    발신번호 등록된 번호 목록 API
    full doc here (https://docs.toast.com/ko/Notification/SMS/ko/api-guide-v2.0/#_59)

    :param use: 번호 사용 여부 (default : True)
    :param block: 번호 차단 여부 (default : False)
    :return: sendNos API request Parameter
    """

    return dict(useYn="Y" if use else "N", blockYn="Y" if block else "N")
