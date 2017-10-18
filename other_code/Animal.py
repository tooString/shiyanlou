#!/usr/bin/env python3
# coding : utf-8


class Animal(object):
    omner = 'jack'

    def __init__(self, name):
        self._name = name

    @classmethod
    def get_owner(cls):
        return cls.omner

    @staticmethod
    def order_animal_food():
        print('ording...')
        print('ok')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print(self.name + 'is making sound wang wang wang...')


class Cat(Animal):
    def make_sound(self):
        print(self.name + 'is making sound miu miu miu...')


if __name__ == '__main__':
    cat = Cat('Kitty')
    print(cat.name)
    Animal.order_animal_food()
