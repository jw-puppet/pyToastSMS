from PyToastSMS import ToastSMSManager

msg = dict(
    _from="01000000000",
    _to="01000000000",  # 발신 번호는 미리 ToastConsole 에서 발신번호로 등록해 놓아야합니다.
    _text="Python Toast SMS Test Message."
)

manager = ToastSMSManager()
response = manager.send_sms(send_no=msg['_from'],
                            recipient_list=[{'recipientNo': msg['_to']}],
                            body=msg['_text'])
print(response)
