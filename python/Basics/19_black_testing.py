import unittest

# Test driven development: Primero organizar las pruebas de la funcion para empezar a escribirla
# To run the test: python -m unittest <filename>

def suma(num_1, num_2):
    return num_1 + num_2

class PrinterError(RuntimeError): ...

class Printer:
    def __init__(self, pages_per_s: float, capacity: int) -> None:
        self.pages_per_s = pages_per_s
        self._capacity = capacity

    def print(self, pages):
        if pages > self._capacity:
            raise PrinterError("Printer does not have enough capacity")
        self._capacity -= pages
        return F"Printed {pages} in {pages/self.pages_per_s:.2f} seconds."


class TestPrinter(unittest.TestCase):
    # The setUp method runs again for each test. 
    # so a new printer will be passed to each test.
    def setUp(self):
        self.printer = Printer(pages_per_s=2.0, capacity=300)

    # If you want the setUp method to run only once
    # Use the setUpClass(cls)
    @classmethod
    def setUpClass(cls) -> None:
        cls.printer = Printer(pages_per_s=2.0, capacity=300)

    # To run something after the tests
    def tearDown(self) -> None:...
    def tearDownClass(cls) -> None:...

    def test_print_within_capacity(self):
        # Tests by default passes if no error is raised
        message = self.printer.print(25)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages = 10
        expected = "Printed 10 pages in 5.00 seconds."
        result = self.printer.print(pages)
        self.assertEqual(result, expected)


    



class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5
        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

    def test_raise_error(self):
        with self.assertRaises(TypeError):
            suma(1, 'a')
        
if __name__ == "__main__":
    unittest.main()