#!/usr/bin/env python
from unittest.mock import Mock

from tools import Calculette, CacluletteScientifique


class TestWithoutMock:
    def setup(self):
        self.calculette = Calculette()

    def test_add(self):
        expected_result = 3 + 4
        returned_result = self.calculette.add(3, 4)
        assert returned_result == expected_result

    def test_sub(self):
        expected_result = 3 - 4
        returned_result = self.calculette.sub(3, 4)
        assert returned_result == expected_result

    def test_mul(self):
        expected_result = 3 * 4
        returned_result = self.calculette.mul(3, 4)
        assert returned_result == expected_result

    def test_div(self):
        expected_result = 3 / 4
        returned_result = self.calculette.div(3, 4)
        assert returned_result == expected_result


class TestWithMock(TestWithoutMock):
    def test_add(self):
        self.calculette.add = Mock()
        self.calculette.add(3, 4)
        self.calculette.add.assert_called_with(3, 4)

    def test_sub(self):
        self.calculette.sub = Mock(return_value=(3-4))
        returned = self.calculette.sub(3, 4)
        expected = self.calculette.sub.return_value
        assert returned == expected


class TestFullMock:
    def test_carre(self):
        # Given
        calculette = Mock(Calculette)
        calculette_scientifique = CacluletteScientifique(calculette)
        # When
        value = 2
        calculette_scientifique.carre(value)
        # Then
        calculette_scientifique.calculette.mul.assert_called_with(value, value)
