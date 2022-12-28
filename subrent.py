#!/usr/bin/env python
import argparse
import logging

from subrent import helper


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
    import os
    logging.info('Starting a reset...')
    open(os.path.join("db", "subrent.db"), "w")


def _import_json_file(options):
    import json
    logging.info('Starting an import...')
    logging.debug(f'{options.json_filename=}')

    zenmoney_json_file = options.json_filename
    transactions = json.load(open(zenmoney_json_file, 'r'))['transaction']
    logging.debug(f"{len(transactions)=}")

    count = helper.import_json(transactions)
    logging.info(f'Imported {count} records')


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
