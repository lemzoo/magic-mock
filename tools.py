#!/usr/bin/env python

def add(first_arg, second_arg):
	return first_arg + second_arg


def add(first_arg, second_arg):
	return first_arg + second_arg


def sub(first_arg, second_arg):
	return first_arg - second_arg


def mul(first_arg, second_arg):
	return first_arg * second_arg


def div(first_arg, second_arg):
	return first_arg / second_arg


class Calculette:
	def __init__(self):
		pass

	def add(self, first_arg, second_arg):
		return add(first_arg,second_arg)

	def sub(self, first_arg, second_arg):
		return sub(first_arg, second_arg)

	def mul(self, first_arg, second_arg):
		return mul(first_arg, second_arg)

	def div(self, first_arg, second_arg):
		return div(first_arg, second_arg)


class CacluletteScientifique:
	def __init__(self, calculette):
		self.calculette = calculette

	def carre(self, value):
		carre = self.calculette.mul(value, value)
		return carre
