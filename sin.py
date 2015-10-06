# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

	

import math

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_prime(self):
        # Набор проверок
        self.assertEqual(lib.sin(0), 0)
        self.assertEqual(lib.sin((math.pi)/2),1)
        self.assertEqual(lib.sin(3*(math.pi)/2),-1)
        self.assertEqual(lib.sin((math.pi)),1)
        



# Запускаем тесты на исполнение
unittest.main(verbosity=2)
