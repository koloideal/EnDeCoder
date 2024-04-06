from helper import helper
import datetime


if __name__ == '__main__':

    with open('traceback.txt', 'a', encoding='utf8') as traceback:

        traceback.write(f'Start logging, datetime: {datetime.datetime.now()}\n\n')

    try:

        helper()

    except KeyboardInterrupt:

        with open('traceback.txt', 'a', encoding='utf8') as traceback:

            traceback.write(f'End logging, datetime: {datetime.datetime.now()}\n\n')

        print('\n\nEnd of work')

        exit()
