from abc import ABC, abstractmethod

GET, SET = "GET", "SET"

class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, kind):
        self._kind = self.kind = kind

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, kind):
        self._kind = (kind, GET)


class EventSet:
    def __init__(self, kind):
        self._kind = self.kind = kind

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        self._kind = (value, SET)


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)



class IntHandler(NullHandler):

    def handle(self, obj, event):
        set_kind = (type(event.kind[0]), SET)

        if event.kind == (int, GET):
            return obj.integer_field

        elif set_kind == (int, SET):
            obj.integer_field = event.kind[0]
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):

    def handle(self, obj, event):
        set_kind = (type(event.kind[0]), SET)

        if event.kind == (float, GET):
            return obj.float_field

        elif set_kind == (float, SET):
            obj.float_field = event.kind[0]
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):

    def handle(self, obj, event):
        set_kind = (type(event.kind[0]), SET)

        if event.kind == (str, GET):
            return obj.string_field

        elif set_kind == (str, SET):
            obj.string_field = event.kind[0]
        else:
            return super().handle(obj, event)

