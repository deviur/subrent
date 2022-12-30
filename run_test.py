# noinspection PyPackageRequirements
import pytest


def run(debug=False):
    arg = '-s' if debug else '-r'
    retcode = pytest.main([arg, 'tests'])
    print(f'{retcode}')


if __name__ == "__main__":
    run()
