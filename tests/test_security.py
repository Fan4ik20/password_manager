import unittest

from security.security import Password


class TestPasswordChecker(unittest.TestCase):
    def test_weak_passwords(self) -> None:
        passwords = ['123123', 'abcdA123asbf', '_Aa123gg', 'simplepass, qwert']

        for password in passwords:
            with self.subTest():
                self.assertFalse(Password.check(password))

    def test_strong_password(self) -> None:
        passwords = [
            'K}sY+):9Fg5D9<AB',
            'L_f7@N(%=KW$e{m9', 'wK73-ze]7gZ)A{Zn'
        ]

        for password in passwords:
            with self.subTest():
                self.assertTrue(Password.check(password))


class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password(self) -> None:
        for _ in range(5):
            with self.subTest():
                self.assertTrue(Password.check(Password.generate(14)))

    def test_raise_error(self) -> None:
        for _ in range(5):
            with self.subTest():
                with self.assertRaises(ValueError):
                    Password.generate(10)


if __name__ == '__main__':
    unittest.main()
