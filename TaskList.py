from __future__ import annotations

from abc import ABC


class Component(ABC):

    @property
    def parent(self) -> Component:
        return self._parent

    # noinspection PyAttributeOutsideInit
    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass


class Leaf(Component):

    def operation(self) -> str:
        return 'leaf'
