class ZeroProductAdd(Exception):
    """
    Проверка на ошибку при добавлении продукта с количеством меньше 0
    """
    def __init__(self, message):
        super().__init__(message)
