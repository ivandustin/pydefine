from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial
from pathlib import Path
import argparse
from tqdm import tqdm
from .process import process
from .read import read


def main():
    args = get_args()
    workers = args.workers
    filepath = args.input
    directory = filepath.parent / filepath.stem
    words = read(filepath)
    function = partial(process, directory)
    with tqdm(total=len(words)) as progress:
        with ThreadPoolExecutor(workers) as executor:
            futures = [executor.submit(function, word) for word in words]
            for _ in as_completed(futures):
                progress.update()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input file", type=Path)
    parser.add_argument("--workers", help="Number of workers", type=int, default=1)
    return parser.parse_args()


if __name__ == "__main__":
    main()
