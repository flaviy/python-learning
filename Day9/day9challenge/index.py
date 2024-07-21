import datetime
from day9challenge import unpack_instructions, get_all_files_from_subfolders, print_results
import re
from collections import namedtuple
import time


def main():
    unpack_instructions.unpack_files('Project+Day+9.zip')
    print('-' * 50)
    print('Search date: ' + datetime.date.today().strftime('%d-%m-%Y'))
    time_start = time.time()
    serial_numbers = []
    pattern = re.compile(r'N\D{3}-\d{5}')
    result = namedtuple('Result', ['filename', 'serial_no'])
    for filename, file in get_all_files_from_subfolders.read_all_files_from_subfolders('unzipped'):
        if filename == 'Instructions.txt':
            continue
        for finding in re.finditer(pattern, file):
            serial_numbers.append(result(filename, finding.group()))

    print_results.print_results(serial_numbers)
    print('Search duration: ', (time.time() - time_start).__ceil__(), ' seconds')


main()
