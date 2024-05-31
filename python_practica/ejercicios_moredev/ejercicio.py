
#  * EJERCICIO:
#  * Crea una función que se encargue de sumar dos números y retornar
#  * su resultado.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un diccionario con las siguientes claves y valores:
#  * "name": "Tu nombre"
#  * "age": "Tu edad"
#  * "birth_date": "Tu fecha de nacimiento"
#  * "programming_languages": ["Listado de lenguajes de programación"]
#  * Crea dos test:
#  * - Un primero que determine que existen todos los campos.
#  * - Un segundo que determine que los datos introducidos son correctos.


import unittest
from datetime import datetime, date

def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    return a + b


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 2.1), 4.6)
        self.assertEqual(sum(2, 2.1), 4.1)
        self.assertEqual(sum(2.5, 2.5), 5)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")
        with self.assertRaises(ValueError):
            sum("a", 7)
        with self.assertRaises(ValueError):
            sum(None, 7)



class TestData(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
            "name": "Pablo Monticoli",
            "age": 24,
            "birth_date": datetime.strptime("28-09-99", "%d-%m-%y").date(),
            "programming_languages": ["Python", "Angular", "Java"]
        }

    def test_fields_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)


unittest.main()
