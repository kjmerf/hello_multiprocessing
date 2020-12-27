import argparse
import logging
import multiprocessing
import os

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


def collatz(positive_int):

    if positive_int % 2 == 0:
        positive_int = positive_int / 2
    else:
        positive_int = 3 * positive_int + 1

    return positive_int


def get_stopping_time(starting_int):

    positive_int = starting_int
    stopping_time = 0
    while positive_int != 1:
        positive_int = collatz(positive_int)
        stopping_time += 1

    logging.info(f"{starting_int} terminated after {stopping_time} steps")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--numbers", dest="numbers", type=int, required=True,
    )
    args = parser.parse_args()

    cpus_to_use = int(os.cpu_count())

    logging.info(f"Processing with {cpus_to_use} CPUs...")
    numbers_processed = 0
    with multiprocessing.Pool(processes=cpus_to_use) as pool:
        for enhanced_ip in pool.imap_unordered(get_stopping_time, range(1, args.numbers+1)):
            numbers_processed += 1
