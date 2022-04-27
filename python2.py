from dhooks import Webhook
def webhook():
    thehook = input("Enter Webhook link : ")
    try:
        while True:
            hook = Webhook(thehook)
            msg = input("Enter The message : ")
            hook.send(msg)
    except:
        print("webhook link error")
        webhook()

webhook()
