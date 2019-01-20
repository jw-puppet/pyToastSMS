# PyToastSMS

Toast Cloud의 SMS Notifiation을 python3에서 쉽게 이용할 수 있는 library 입니다.


######
Toast Cloud SMS API Docs : https://docs.toast.com/ko/Notification/SMS/ko/Overview/

#### SMS API Version
 - 2.0
 
#### 구현된 기능
 - send_sms (단문 SMS 발송)
 - send_mms (장문 MMS 발송;첨부파일 미구현)
 - list_sent_sms (발송된 SMS 목록)
 - list_send_nos (발신번호로 등록된 번호 목록)


#### How to use
 - ToastCloud 가입 후 app 을 생성하고 app_key 를 "config/secret.yml"의 app_key 를 넣어주기만 하면 됩니다.
 - 국내법 상 발신 번호는 사전에 인증된 번호만 사용 가능합니다. ToastConsole 에서 발신번호로 사용할 번호를 등록 후 이용해 주세요.
 - 단문 sms 발신 예제 "examples/send_sms.py" 를 참고하세요.
 
 #### License
 MIT License