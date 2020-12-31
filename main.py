import argparse

import requests

BASE_URL = (
    "http://dl.stickershop.line.naver.jp/products/0/0/1/%s/iphone/stickerpack@2x.zip"
)


DEFAULT_OUTPUT_NAME = "output"

BASE_OUTPUT = "%s.zip"


def main():
    parser = argparse.ArgumentParser(description="download line sticker as zip")
    parser.add_argument("id", help="sticker id")
    parser.add_argument("--name", help="output name", default=DEFAULT_OUTPUT_NAME)
    args = parser.parse_args()

    url = BASE_URL % args.id
    print("downloading %s" % url)

    rsp = requests.get(url)
    if rsp.status_code == 200:
        output = BASE_OUTPUT % args.name
        print("saving %s" % output)
        with open(output, "wb") as f:
            f.write(rsp.content)
    else:
        print("failed with status", rsp.status_code)


if __name__ == "__main__":
    main()
