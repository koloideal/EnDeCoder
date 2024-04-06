from helper import helper
import datetime


if __name__ == '__main__':

    with open('traceback.txt', 'a', encoding='utf8') as traceback:

        start_now = datetime.datetime.now()

        traceback.write(f'Start logging, datetime: {start_now}\n\n')

    try:

        helper()

    except KeyboardInterrupt:

        with open('traceback.txt', 'a', encoding='utf8') as traceback:

            end_now = datetime.datetime.now()

            traceback.write(f'Script running time: {end_now - start_now}\n')

            traceback.write(f'End logging, datetime: {end_now}\n\n')

        print('\n\nEnd of work')

        exit()
