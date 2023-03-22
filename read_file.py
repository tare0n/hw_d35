import time
import os


def read_file_timed(file):
    start_time = time.time()
    try:
        bin_data = open(file, 'rb')
        if not os.path.isfile(file):
            raise FileNotFoundError
    except FileNotFoundError:
        print(f"No such file or directory: '{file}'")
        final_time = 0.0
    else:
        final_time = time.time() - start_time
    finally:
        print(f"Time required for '{file}' = {final_time}'")
