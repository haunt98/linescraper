import argparse

import requests

BASE_URL = (
    "http://dl.stickershop.line.naver.jp/products/0/0/1/%s/iphone/stickerpack@2x.zip"
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("id", help="line sticker id")
    args = parser.parse_args()

    url = BASE_URL % args.id
    print("url", url)

    rsp = requests.get(url)
    if rsp.status_code == 200:
        with open("%s.zip" % args.id, "wb") as f:
            f.write(rsp.content)
    else:
        print("failed with status", rsp.status_code)


if __name__ == "__main__":
    main()
