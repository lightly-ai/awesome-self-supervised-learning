## References
# * https://github.com/SkalskiP/awesome-foundation-and-multimodal-models/blob/master/automation/generate.py

import argparse

HEADER: str = """# Awesome Self Supervised Learning [![awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    content = HEADER

    ## Write to file
    with open("README.md", "w") as f:
        f.write(content)
