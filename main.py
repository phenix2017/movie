import requests
from bs4 import BeautifulSoup
import pdb

class SpiderGoT:
    def __init__(self):
        self.url_tmp = 'http://m.zimuzu.tv/resource/item?rid=%s&season=%s&episode=%s'
        self.rid = '10760'
        self.season = 1  # 目前总共有 8 季
        self.episode = 1  # 每季 12 集
        self.ed2k_urls_list = []
        self.save_file_name = 'urls.txt'

    def run(self):
        while True:
            try:
                response = requests.get(self.url_tmp % (self.rid, self.season, self.episode))
                soup = BeautifulSoup(response.text, "lxml")
                pdb.set_trace()
                ed2k_url = soup.find('a', class_='copy')['data-url']
                result_str = '第 %s 季，第 %s 集\n%s' % (self.season, self.episode, ed2k_url)
                self.ed2k_urls_list.append(result_str)
                print(result_str)
            except TypeError as e:
                print('采集结束')
                self.write_file()
                break
            self.update_season_episode()

    def update_season_episode(self):
        self.episode += 1
        if self.episode >= 12:
            self.episode = 1
            self.season += 1

    def write_file(self):
        with open(self.save_file_name, 'w') as f:
            for url in self.ed2k_urls_list:
                f.write(str(url) + '\n')
        print('所有链接保存在 urls.txt 文件中')





if __name__ == '__main__':
    spider = SpiderGoT()
    spider.run()
