from abc import ABC, abstractmethod, abstractclassmethod


class AbstractEffect(Hero, ABC):
    def __init__(self, decorated_obj):
        self.base = decorated_obj

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_stats(self):
        stats = self.base.get_stats()

        for key in self.buff.keys():
            stats[key] += self.buff[key]

        return stats

    @property
    @abstractmethod
    def buff(self):
        pass

    def __str__(self):
        return self.__class__.__name__


class AbstractPositive(AbstractEffect, ABC):

    def get_positive_effects(self):
        result = self.base.get_positive_effects()
        result.append(self.__str__())
        return result

    @property
    @abstractmethod
    def buff(self):
        pass


class Berserk(AbstractPositive):
    _buff = {
            "HP": 50,  # health points
            "Strength": 7,  # сила
            "Perception": -3,  # восприятие
            "Endurance": 7,  # выносливость
            "Charisma": -3,  # харизма
            "Intelligence": -3,  # интеллект
            "Agility": 7,  # ловкость
            "Luck": 7  # удача
        }

    @property
    def buff(self):
        return self._buff



class Blessing(AbstractPositive):
    """увеличивает все основные характеристики на 2."""
    _buff = {
            "Strength": 2,  # сила
            "Perception": 2,  # восприятие
            "Endurance": 2,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 2,  # интеллект
            "Agility": 2,  # ловкость
            "Luck": 2  # удача
        }

    @property
    def buff(self):
        return self._buff


class AbstractNegative(AbstractEffect):

    def get_negative_effects(self):
        result = self.base.get_negative_effects()
        result.append(self.__str__())
        return result

    @property
    @abstractmethod
    def buff(self):
        pass


class Weakness(AbstractNegative):
    _buff = {
            "Strength": -4,  # сила
            "Endurance": -4,  # выносливость
            "Agility": -4,  # ловкость
    }

    @property
    def buff(self):
        return self._buff


class Curse(AbstractNegative):
    _buff = {
            "Strength": -2,  # сила
            "Perception": -2,  # восприятие
            "Endurance": -2,  # выносливость
            "Charisma": -2,  # харизма
            "Intelligence": -2,  # интеллект
            "Agility": -2,  # ловкость
            "Luck": -2  # удача
        }

    @property
    def buff(self):
        return self._buff


class EvilEye(AbstractNegative):
    _buff = {
            "Luck": -10  # удача
        }

    @property
    def buff(self):
        return self._buff


