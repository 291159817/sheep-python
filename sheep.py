"""
@author : you
羊了个羊 通关脚本
"""
import requests
import time
from config import *

headers = {
    "Host": "cat-match.easygame2021.com",
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4455.2 Safari/537.36',
    "t": TOKEN,
}


def pass_game():
    """
    get请求接口直接通关
    :return:True or False
    """
    url = 'https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time=4&rank_role=1&skin=1'
    res = requests.get(url=url, headers=headers, timeout=5)
    # print(res.text)
    if res.json()["err_code"] == 0:
        print("\033[1;31m----------闯关成功----------\033[0m")
        return True
    else:
        print(res.json())
        print("token错误!")
        return False


if __name__ == '__main__':
    run_count = RUN_COUNT
    success = 0
    for i in range(0, run_count):
        try:
            print("正在尝试请求接口！")
            flag = pass_game()
            if flag:
                success = success + 1
                print("\033[1;31m当前已经闯关成功第{}次\033[0m".format(success))
                print("\033[1;31m--------------------------\033[0m")
                time.sleep(SlEEP_TIME)
            else:
                break
        except Exception as e:
            print("接口请求超时！错误原因：", e)
