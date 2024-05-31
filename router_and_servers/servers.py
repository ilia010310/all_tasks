from data import Data
import logging

logger = logging.getLogger(__name__)


class Server:
    """Класс для описания работы сервера в сети"""
    __ip_counter = 0

    def __init__(self) -> None:
        """buffer - список принятых пакетов
        ip - IP-адрес текущего сервера
        """
        Server.__ip_counter += 1
        self.buffer = []
        self.ip = Server.__ip_counter
        self.connect = False

    def send_data(self, data: Data) -> None:
        """Отправляет информационный пакет data(объкет класса Data)
        с указанным IP адресом получателя (пакет отправляется роутеру
        и сохраняется в его буфере(локальное свойство buffer)"""
        if self.connect:
            self.connect.set_buffer(data)
        else:
            logger.error('Ошибка: нет связи с роутером')

    def get_data(self) -> list:
        """Возвращает список принятых пакетов (если ничего принято не было,
        то возвращается пустой список),
        и очищает входной буфер"""
        if self.buffer == []:
            return []
        response = []
        for data in self.buffer:
            response.append(data.get_msg())
        self.buffer = []
        return response

    def get_ip(self) -> int:
        """Возвращает свой IP адрес"""
        return self.ip

    def add_buffer(self, data: Data) -> None:
        self.buffer.append(data)
