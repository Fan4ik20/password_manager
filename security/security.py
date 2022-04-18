from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random


class _SecurePassword:
    _min_length = 14
    _potential_vulnerabilities = {
        'ascii_lowercase':
            'Password must contain at least one lowercase letter',
        'ascii_uppercase':
            'Password must contain at least one uppercase letter',
        'digits': 'Password must contain at least one digit',
        'punctuation': 'Password must contain at least one special character',
        'length': f'Password must be at least {_min_length} length long',
    }


class _PasswordChecker(_SecurePassword):
    @staticmethod
    def _define_success_condition(symbol: str, vulnerabilities: dict) -> None:
        if symbol in ascii_lowercase and vulnerabilities.get(
                'ascii_lowercase'
        ):
            vulnerabilities['ascii_lowercase'] = False

        elif symbol in ascii_uppercase and vulnerabilities.get(
                'ascii_uppercase'
        ):
            vulnerabilities['ascii_uppercase'] = False

        elif symbol in digits and vulnerabilities.get('digits'):
            vulnerabilities['digits'] = False

        elif symbol in punctuation and vulnerabilities.get('punctuation'):
            vulnerabilities['punctuation'] = False

    @classmethod
    def _find_vulnerabilities(cls, password: str) -> dict:
        vulnerabilities = {
            'ascii_lowercase': True,
            'ascii_uppercase': True,
            'digits': True,
            'punctuation': True,
            'length': True if len(password) < 14 else False,
        }

        for symbol in set(password):
            cls._define_success_condition(symbol, vulnerabilities)

        return vulnerabilities

    @classmethod
    def check(cls, password: str) -> bool:
        vulnerabilities = cls._find_vulnerabilities(password)

        if not any(vulnerabilities.values()):
            print('Strong Password')

            return True

        print('Weak Password')

        for vulnerability, existence in vulnerabilities.items():
            if existence:
                print(cls._potential_vulnerabilities[vulnerability])

        return False


class _PasswordGenerator(_SecurePassword):
    available_symbols = (
            ascii_uppercase + ascii_lowercase + digits + punctuation
    )

    @staticmethod
    def _generate_necessary_symbols() -> list:
        necessary_symbols = [
            random.choice(ascii_uppercase),
            random.choice(ascii_lowercase),
            random.choice(digits),
            random.choice(punctuation)
        ]

        return necessary_symbols

    @classmethod
    def _generate_secure_password(cls, length: int) -> str:
        password = [
            random.choice(cls.available_symbols) for _ in range(length - 4)
        ] + cls._generate_necessary_symbols()

        random.shuffle(password)

        return ''.join(password)

    @classmethod
    def generate(cls, length: int) -> str:
        if length < 14:
            raise ValueError(
                cls._potential_vulnerabilities['length']
            )

        secure_password = cls._generate_secure_password(length)

        return secure_password


class Password:
    @staticmethod
    def check(password: str) -> bool:
        return _PasswordChecker.check(password)

    @staticmethod
    def generate(length: int) -> str:
        return _PasswordGenerator.generate(length)
