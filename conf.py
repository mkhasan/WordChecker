
class Conf:
    HSOT = "localhost"
    USER = "root"
    PASSWD = "test123"
    DATABASE = "TEST_DB"
    TABLENAME = "words_1"


    FONT_SIZE_LARGE = 14
    FONT_SIZE_NORMAL = 12
    FONT_SIZE_SMALL = 8
    FONT_NAME_LARGE = 'TkDefaultFont'
    FONT_NAME_NORMAL = FONT_NAME_LARGE
    FONT_NAME_SMALL = FONT_NAME_LARGE

    START_WITH_RANDOMNESS = False

    READ_FROM_EXCEL_FILE = True


    SEQ_PLACE = 1
    RANDOM_PLACE = 2

    class MyException(Exception):
        def __init__(self, message):
            self.message = message

        def __str__(self):
            return "Error: " + self.message


