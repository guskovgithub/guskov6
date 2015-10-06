# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_factorial_non_negative_arg(self):
        # Набор проверок
        self.assertEqual(lib.factorial(1), 1)
        self.assertEqual(lib.factorial(3), 6)
        self.assertEqual(lib.factorial(5), 120)
        self.assertEqual(lib.factorial(0), 1)
    def test_factorial_negative(self):
        # Набор проверок
        self.assertEqual(lib.factorial(-1), 1)
        self.assertEqual(lib.factorial(-5), 1)


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
