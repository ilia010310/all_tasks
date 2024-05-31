class Data:
    """Класс для описания пакета информации"""

    def __init__(self, data: str = '', ip: int = 1) -> None:
        """data - передаваемые данные
        ip - IP-адрес назначения"""
        self.data: str = data
        self.ip = ip

    def get_msg(self):
        return self.data
