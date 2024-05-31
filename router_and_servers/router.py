import logging

from servers import Server

logger = logging.getLogger(__name__)

class Router:
    """Класс для описания работы роутеров в сети
    (в данной задаче пологается один роутер)"""

    def __init__(self) -> None:
        """buffer - буфер роутера
        links_servers - сервера, которые имеют связь с роутером"""
        self.buffer = []
        self.links_servers = {}

    def link(self, server: Server) -> None:
        """Присоединяет сервер(объект класса Server) к роутеру
        для простоты, каждый сервер соединен только с одним роутером"""
        self.links_servers[server.ip] = server
        server.connect = self

    def unlink(self, server: Server) -> None:
        """Отсоединяет сервер(объект класса Server) от роутера"""
        del self.links_servers[server.ip]
        server.connect = False

    def send_data(self) -> None:
        """Отправляет все пакеты(объект класса Data) из буфера роутера
        соответствующим серверам (после отправки буфер должен очищаться)"""
        if self.buffer:
            for data in self.buffer:
                if data.ip in self.links_servers:
                    send_to = data.ip
                    server = self.links_servers[send_to]
                    server.add_buffer(data)
            self.buffer = []
        else:
            logger.warning('Нет пакетов для рассылок')

    def set_buffer(self, data) -> None:
        """Добавляет элемент в буфер роутера"""
        self.buffer.append(data)
