class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

class Bulldog(Dog):

    def sleep(self):
        return 'snoring!'

teddy = Dog()
print(teddy.speak())  # bark!
print(teddy.sleep())  # sleeping!

bonbon = Bulldog()
print(bonbon.speak()) # bark!
print(bonbon.sleep()) # snoring!
