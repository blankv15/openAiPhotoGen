from openai import OpenAI


class Image:

    def __init__(self, prompt):
        self.client = OpenAI()
        self.model = "dall-e-3"
        self.prompt = prompt
        self.defaultSize = "1024x1024"
        self.quality = "standard"
        self.n = 1
        self.response = ""

    def continueCheck(self):
        continue_check = input("Are you sure you want to overwrite? press y/n")
        if continue_check == "y" or continue_check == "Y":
            return True
        return False

    def createImage(self):
        if self.response == "":
            self.response = self.client.images.generate(
                model=self.model,
                prompt=self.prompt,
                size=self.defaultSize,
                quality=self.quality,
                n=self.n,
            )
            print(self.response.data[0].url)
            return self.response.data[0].url


    def getResponse(self):
        return self.response

    def getResponseData(self):
        return(self.response.data)

    def getImageUrl(self):
        return  self.response.data[0].url

