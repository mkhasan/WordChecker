
class MyException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return "MT error: " + self.message

def main():


    x = int(input("Please enter a number: "))
    if x > 7:
        raise MyException("msg")

    print("here")



if __name__ == '__main__':

    try:
        main()
    except Exception as e:      # accepting Exception means accepting all exception
        print(e)