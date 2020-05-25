import time
import subprocess
import sys
import logging


def generate(directory=".") -> str:
    return time.strftime(
        "%y.%j.%k%M%S",
        time.localtime(
            int(
                subprocess.check_output(
                    "git show -s --format='%ct'", shell=True, cwd=directory
                )
                .decode()
                .strip()
            )
        ),
    )


if __name__ == "__main__":
    try:
        print(generate(**dict(arg.split("=") for arg in sys.argv[3:])))
    except Exception as e:
        logging.exception("%s Crashed, Error: %s", "[DateVersioning]", e)
