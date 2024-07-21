'''
The on-screen presentation of the findings should be a list in table format, respecting the following example format:


FILE		SERIAL NO.
----		----------
text1.txt 	Nter-15496
text25.txt 	Ngba-85235

'''


def print_results(serial_numbers):
    print('FILE\t\t\tSERIAL NO.')
    print('----\t\t\t----------')
    for file, serial in serial_numbers:
        print(f'{file}\t\t{serial}')

    print('Numbers found: ', len(serial_numbers))
