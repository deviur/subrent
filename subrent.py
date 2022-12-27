#!/usr/bin/env python
import argparse
import logging


def _parse(argv):
    parser = argparse.ArgumentParser(description='Get an income report for a day')
    parser.add_argument('-D', '--debug', action='store_true', default=False, help="set debug logging level")
    subparsers = parser.add_subparsers(dest='command', required=True)
    reset_parser = subparsers.add_parser('reset', help="Reset Subrent's database")
    import_parser = subparsers.add_parser('import', help="Import ZenMoney's json file to Subrent's database")
    import_parser.add_argument('json_filename', action='store', help="ZenMoney's json file")
    report_parser = subparsers.add_parser('report', help="Get a report")
    report_parser.add_argument('date', action='store')
    return parser.parse_args(argv[1:])


def _reset(options):
    logging.info('Starting a reset...')


def _import_json_file(options):
    logging.info('Starting an import...')
    logging.debug(f'{options.json_filename=}')


def _report(options):
    logging.info(f'Starting a report...')
    logging.debug(f'{options.date=}')


def runner(options):
    logging.debug(f'Starting runner...\n{options=}')
    return COMMANDS[options.command](options)


COMMANDS = {
    'reset': _reset,
    'import': _import_json_file,
    'report': _report,
}

if __name__ == "__main__":
    import sys
    args = _parse(sys.argv)
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    runner(args)
