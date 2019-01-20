"""
수신자, 수신자 목록 객체
"""
from typing import List, Union

import enforce


class Recipient(object):
    @enforce.runtime_validation
    def __init__(self, recipient_number: str, countryCode: str = None, internationalRecipientNo: str = None,
                 templateParameter: dict = None):
        """
        :param recipient_number: (필수) 수신자 번호
        :param countryCode: (옵션) 국가번호
        :param internationalRecipientNo: (옵션) 국가번호 포함 수신자 번호. recipient_number 지정 시 무시됨.
        :param templateParameter: (옵션) 템플릿 아이디 입력 시 템플릿 치환용 {key:value} 오브젝트
        """

        # Required
        self.recipientNo: str = recipient_number

        # Optional
        self.countryCode: str = countryCode
        self.internationalRecipientNo: str = internationalRecipientNo
        self.templateParameter: dict = templateParameter

    def to_dict(self) -> dict:
        """
        :return: 사용되지 않은 Key(dict[Key] is None)를 제외한 단일 수신자 인스턴스 dictionary 객체를 반환.
        """
        return {k: v for k, v in self.__dict__.items() if v is not None}

    def to_list(self) -> List[dict]:
        """
        :return: 사용되지 않은 Key(dict[Key] is None)를 제외한 단일 수신자 인스턴스 dictionary 객체를 List Type 으로 wrapping 하여 반환.
        """
        return [self.to_dict(), ]


class RecipientList(object):
    """
    Recipient 를 List Type 으로 보관 하는 객체.
    """

    def __init__(self):
        self.list: List = []

    @enforce.runtime_validation
    def append(self, recipient: Recipient) -> None:
        """
        Recipient 객체를 self.list 에 추가함.
        """
        self.list.append(recipient)

    @enforce.runtime_validation
    def add_recipients(self, recipient_list: List[List[Union[str, dict]]]) -> int:
        """
        대량의 수신자를 한번에 추가 하기 위한 메서드.
        :param recipient_list: [[recipient_number, (country_code), (internationalRecipientNumber), (templateParameter),]
                                2차원 리스트 형으로 Recipient.__init__() 인자를 순서대로 입력.
        :return 수신자를 전부 추가 후 RecipientList.list 원소 개수 반환.
        """
        for recipient in recipient_list:
            self.append(Recipient(*recipient))

        return len(self)

    def flush(self):
        """
        self.list 를 flush 함.
        """
        self.list = []

    def __len__(self):
        """
        :return: self.list (수신자 객체 수) 를 반환.
        """
        return len(self.list)

    def to_list(self) -> List[dict]:
        """
        :return: self.list 에 있는 수신자 객체 각각을 dictionary Type 으로 변환한 리스트를 반환.
        """
        return list(r.to_dict() for r in self.list)
