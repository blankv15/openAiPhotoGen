from openai import OpenAI


class AItextAssistant:

    def __init__(self):
        self.client = OpenAI()
        self.model = "gpt-4"
        self.messages = []
        self.completion = ""
        self.messageHistory = []

    def sendRequest(self):
        self.completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        print(self.completion.choices[0].message)
        self.messageHistory.append(self.completion)

    def updateSystem(self,prompt):
        self.messages.append(
            {"role": "system",
             "content": prompt}
        )

    def askQuestion(self,prompt):
        self.messages.append(
            {"role": "user",
             "content": prompt}
        )

    def setMessages(self,messages):
        self.messages = messages

        self.sendRequest()


