import unittest
import DateVersioning


class TestDateVersioning(unittest.TestCase):
    def test_format(self):
        self.assertRegex(DateVersioning.generate(), "\d{2}.\d{3}.\d{6}")


if __name__ == "__main__":
    unittest.main()
