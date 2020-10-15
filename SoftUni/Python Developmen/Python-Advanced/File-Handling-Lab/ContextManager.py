class CM:
    def __init__(self, file_name, mode):
        self.__file_name = file_name
        self.__mode = mode

    def __enter__(self):
        self.__file_handle = open(self.__file_name)
        return self.__file_handle

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file_handle.close()


with CM() as some_value:
    print(some_value)
    print("baba")
