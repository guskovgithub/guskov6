# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_prime(self):
        # Набор проверок
        self.assertEqual(lib.prime(3), True)
        self.assertEqual(lib.prime(0), False)
        self.assertEqual(lib.prime(7), True) 
        self.assertEqual(lib.prime(6), False)
        self.assertEqual(lib.prime(1), False)
   

# Запускаем тесты на исполнение
unittest.main(verbosity=2)
