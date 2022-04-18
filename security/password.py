import argparse

from security.security import Password


class PasswordCLI:
    def __init__(self) -> None:
        self._parser = argparse.ArgumentParser()
        self._parser.add_argument(
            '--generate', type=int,
            help='Generates a new secure password of the specified length'
        )
        self._parser.add_argument(
            '--check', type=str,
            help='Checks the given password for security'
        )

        self.args = None

    def _parse_args(self) -> None:
        self.args = self._parser.parse_args()

    def process_request(self) -> None:
        self._parse_args()

        if pass_len := self.args.generate:
            print(Password.generate(pass_len))

        elif password := self.args.check:
            Password.check(password)


def main() -> None:
    password_cli = PasswordCLI()
    password_cli.process_request()


if __name__ == '__main__':
    main()
