# from credentials import mobile_number
import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : "{{Mobile Number}}",
        'message': 'Hey, Good morning',
        'key': 'db565dd5a3c0a048e70f5a133591f99f2c3b913cfIteMUqYBH8blgeJimB7pZKn5'
    })
    print(resp.json())

# schedule.every() .day.at('06:00').do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
