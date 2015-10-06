# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_even(self):
        # Набор проверок
        self.assertEqual(lib.even(4), True)
        self.assertEqual(lib.even(1), False)
        self.assertEqual(lib.even(5), False)
        self.assertEqual(lib.even(17), False)
        
        self.assertEqual(lib.even(-2), True)
        self.assertEqual(lib.even(-5), False)
        self.assertEqual(lib.even(-7), False)   
 

# Запускаем тесты на исполнение
unittest.main(verbosity=2)
