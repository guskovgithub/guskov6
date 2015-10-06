# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

	

import math

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_palindrome(self):
        # Набор проверок
        self.assertEqual(lib.palindrome('44'), True)
        self.assertEqual(lib.palindrome('125'), False)
        self.assertEqual(lib.palindrome('ooooo'), True)
        self.assertEqual(lib.palindrome('858'), True)
        self.assertEqual(lib.palindrome('kuiouiglt'), False)

        
     


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
