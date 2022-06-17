from unittest import TestCase
from unittest.mock import patch
from page import PageRequester

class TestPageRequester(TestCase):
    def setUp(self) -> None:
        self.page = PageRequester("https://google.com")

    # Para hacer test de librerias se usa un mock de una 
    # funcion para evitar hacerle test al codigo de la libreria.
    # Ej: asegurar que se llama el metodo requests.get
    def test_make_request(self):
        with patch("requests.get") as mocked_get:
            self.page.get()
            mocked_get.assert_called()


    def test_content_returned(self):
        fake_content = "Hello"
        class FakeResponse:
            def __init__(self) -> None:
                self.content = fake_content

        with patch("requests.get", return_value=FakeResponse()) as mocked_get:
            result = self.page.get()
            self.assertEqual(result, fake_content)