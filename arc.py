import smtplib

import config

def RealTimeCurrencyExchangeRate() :
    import requests, json
    req_ob = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=GBP&to_currency=INR&apikey=Q91KNQD5U1QCX3DY")
    result = req_ob.json() 
    
    GBP_INR = result["Realtime Currency Exchange Rate"]['5. Exchange Rate']
    
    return(GBP_INR)

Exchange_Rate = RealTimeCurrencyExchangeRate() 

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.RECIEVER_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")

subject = "Exchange_Rate"
msg = "Current Exchange Rate is above the threshold, Right now it is " + Exchange_Rate
threshold = 87.0

if(float(Exchange_Rate) > threshold):
    send_email(subject, msg)
