import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

# PRUEBA SUMA EXITO
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))


# PRUEBA SUMA FALLO
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())


# PRUEBA RESTA FALLO
    def test_substract_method_raises_type_error(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

# PRUEBA MULTIPLICACION EXITO
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

# PRUEBA MULTIPLICACION FALLO
    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

# PRUEBA DIVISION EXITO
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

# PRUEBA DIVISION FALLO
    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

# PRUEBA DIVISION POR 0
    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

# PRUEBA POTENCIA EXITO
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(1, self.calc.power(10, 0))
        self.assertEqual(0.25, self.calc.power(2, -2))

# PRUEBA POTENCIA TIPO ERROR
    def test_power_method_raises_type_error(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())

# PRUEBA RAIZ EXITO
    def test_square_root_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.square_root(4))
        self.assertEqual(3, self.calc.square_root(9))
        self.assertEqual(0, self.calc.square_root(0))
        self.assertAlmostEqual(1.414, self.calc.square_root(2), places=3)
    
    # PRUEBA LOGARITMO RAISES VALUE ERROR
    def test_sqaure_root_method_raises_value_error(self):
        self.assertRaises(ValueError, self.calc.logarithm, -2)
        self.assertRaises(TypeError, self.calc.logarithm, "-1")


# PRUEBA LOGARITMO EXITO
    def test_logarithm_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.logarithm(100))
        self.assertAlmostEqual(0.434, self.calc.logarithm(2.71828), places=3)
        self.assertEqual(0, self.calc.logarithm(1))

# PRUEBA LOGARITMO RAISES VALUE ERROR
    def test_logarithm_method_raises_value_error(self):
        self.assertRaises(ValueError, self.calc.logarithm, -2)
        self.assertRaises(ValueError, self.calc.logarithm, 0)
        self.assertRaises(TypeError, self.calc.logarithm, "-1")
        self.assertRaises(TypeError, self.calc.logarithm, "0")



if __name__ == "__main__":  # pragma: no cover
    unittest.main()
