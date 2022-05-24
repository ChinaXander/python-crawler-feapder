# -*- coding: utf-8 -*-
"""
@Time           :2022/5/24
@author         :XDS
@Description    :
"""
import filetype
from feapder.utils.tools import *


def is_Chinese(word):
    """
    判断是否为中文
    :param word:
    :return:
    """
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def download(url, path=None, file_name=None, headers=None, proxies=None):
    """
    下载文件
    :param proxies:
    :param headers:
    :param file_name: 文件名
    :param path: 文件路径
    :param url: 图片网络地址
    :return:{'file_name': file_name, 'oss_path': oss_path}
    """
    if path:
        path = os.getcwd() + '/download/' + path
    else:
        path = os.getcwd() + '/download/'

    mkdir(path)

    # 文件名称
    suf = None
    if not file_name:
        file_name = hashlib.sha1(url.encode('utf-8')).hexdigest()  # 生成文件名称
        url = re.sub(r"\?.*", '', url)  # 去除?及后面的参数
        url = re.sub(r"#.*", '', url)  # 去除#及后面的参数
        suf = url.split("/")[-1].split('.')[-1]  # 获取文件后缀
        if suf:
            file_name += f".{suf}"

    # 文件本地地址
    file_path = path + file_name

    if not download_file(url, file_path):
        try:
            response = requests.get(url, headers=headers, proxies=proxies).content
            f = open(path + file_name, 'wb')
            f.write(response)
            f.close()
        except Exception as e:
            log.warning(f"文件下载失败[{url}]>>>{e}")
            return False

    if not suf:
        filet = filetype.guess('download/447d4c95612fa46ad793f5f2d26ac1dfad0c6e3dpng')
        new_file_name = f"{file_name}.{filet.extension}"
        os.rename(file_path, new_file_name)

    log.info(f"文件下载成功[{file_path}]>>>{url}")
    return True
