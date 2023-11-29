# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import re

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MonsterSirenPipeline:

    def process_item(self, item, spider):
        """
        接受数据并保存
        OSError: [WinError 123] 文件名、目录名或卷标语法不正确。: 'music/0:00:01'
        :param item:
        :param spider:
        :return:
        """
        name = item['name']
        data = item['source']
        album_id = item['album_id']
        is_album = item['is_album']
        suffix = item['suffix']
        # 部分歌曲名有非法字符，此处替换
        while name != re.sub(r'[\\/:*?<>"|]', '!', name):
            name = re.sub(r'[\\/:*?<>"|]', '!', name)

        if not os.path.exists('music'):
            os.mkdir('music')

        if not os.path.exists('music/{}'.format(album_id)):
            os.mkdir('music/{}'.format(album_id))
        file_path = ''
        if is_album is True:
            file_path = 'music/{}/{}.jpg'.format(album_id,name)

        else:
            file_path = 'music/{}/{}.{}'.format(album_id,name,suffix)
        
        with open(file_path,'wb') as fq:
            fq.write(data)
        return item
