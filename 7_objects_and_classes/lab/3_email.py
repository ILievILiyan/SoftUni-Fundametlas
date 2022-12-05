class Email:

    def __init__(self, sender_, receiver_, content_):
        self.sender = sender_
        self.receiver = receiver_
        self.content = content_
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while True:
    command = input()
    if command == "Stop":
        break
    sender, receiver, content = command.split(" ")
    email = Email(sender, receiver,content)
    emails.append(email)

indexes = input().split(", ")
send_emails = [emails[int(x)].send() for x in indexes]

for email in emails:
    print(email.get_info())






