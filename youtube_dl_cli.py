# from __future__ import unicode_literals
import os
import re

import youtube_dl


def main():
    print("#=====================================#")
    print("#          默认下载720P视频(y/n)      #")
    print("#=====================================#")
    a = input("输入空格键继续(输入n则进行其它选择):")
    if a == "n":
        print("#====================================#")
        print("#============= 请选择 ===============#")
        print("#====================================#")
        print("#                                    #")
        print("# [11] 下载 list.txt 里的东西(720P)  #")
        print("#                                    #")
        print("# [12] 下载 list.txt 里的东西(1080p) #")
        print("#                                    #")
        print("# [21] 输入地址下载720P视频          #")
        print("#                                    #")
        print("# [22] 输入地址下载1080P视频         #")
        print("#====================================#")
        d = input("\n->[?] 输入序号：")
        if d == "11":
            download1(get_urls("list.txt"))
        if d == "12":
            download2(get_urls("list.txt"))
        if d == "21":
            while True:
                b = []
                b.append(input("\n->[!] 输入视频所在网页地址并回车开始下载：\n"))
                download1(b)
        if d == "22":
            while True:
                c = []
                c.append(input("\n->[!] 输入视频所在网页地址并回车开始下载：\n"))
                download2(c)
    else:
        while True:
            b = []
            b.append(input("\n->[!] 输入视频所在网页地址并回车开始下载：\n"))
            download1(b)


def download1(dl_list: list):
        ydl_opts = {
                        'format': 'bestvideo[height <=? 720][ext=mp4]+bestaudio[ext=m4a]/best[height <=? 720]/best', 
                    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(dl_list)
            # ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
    
    


def download2(dl_list: list):
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
