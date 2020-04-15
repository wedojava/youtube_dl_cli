# from __future__ import unicode_literals
import os
import re

import youtube_dl


def main():
    print("#===========================#")
    print("#========= 请选择 ==========#")
    print("#===========================#")
    print("#                           #")
    print("# [1] 下载 list.txt 里的东西#")
    print("#                           #")
    print("# [2] 直接给地址下载        #")
    print("#                           #")
    print("#===========================#")
    a = input("\n->[?] 输入序号：")
    if a == "1":
        download(get_urls("list.txt"))
    if a == "2":
        while True:
            b = []
            b.append(input("输入视频所在网页地址："))
            download(b)


def download(dl_list: list):
    ydl_opts = {
        'format': 'bestvideo[height <=? 1080][ext=mp4]+bestaudio[ext=m4a]/best[height <=? 1080]/best',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(dl_list)
        # ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])


def get_urls(filepath: str) -> list:
    """Get url list from file. Just urls without other text."""

    l_urls = _list = []
    if not os.path.lexists(filepath):
        return None
    try:
        with open(filepath, encoding='gbk') as f:
            _list = f.read().splitlines()
    except Exception:
        with open(filepath, encoding='utf8') as f:
            _list = f.read().splitlines()

    regex = r"([^\\/:*?\"<>|!]*)[|]?(https://.*)"
    for i in _list:
        if i == '':
            continue
        else:
            m = re.search(regex, i)
            l_urls.append(m.group(2))

    return l_urls


if __name__ == '__main__':
    main()
