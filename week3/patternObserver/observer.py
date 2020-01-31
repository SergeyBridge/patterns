from abc import ABC, abstractmethod


class ObservableEngine(Engine):
    def __init__(self):
        self.__observers = set()

    def subscribe(self, observ):
        self.__observers.add(observ)

    def unsubscribe(self, observ):
        self.__observers.remove(observ)

    def notify(self, msg):
        for observ in self.__observers:
            observ.update(msg)


class AbstractObserver(ABC):
    def __init__(self):
        self._achievements = []
        self._achievements_set = set()

    @abstractmethod
    def update(self):
        pass

    @property
    @abstractmethod
    def achievements(self):
        return self._achievements


class ShortNotificationPrinter(AbstractObserver):

    def update(self, msg):
        self._achievements_set.add(msg["title"])

    @property
    def achievements(self):
        return self._achievements_set


class FullNotificationPrinter(AbstractObserver):

    def update(self, msg):
        if msg["title"] not in self._achievements_set:
            self._achievements_set.add(msg["title"])
            self._achievements.append(msg)

    @property
    def achievements(self):
        return self._achievements
