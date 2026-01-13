class Pet:
    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Pet):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'
