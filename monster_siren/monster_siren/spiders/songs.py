from monster_siren.items import MonsterSirenItem
from jsonpath import jsonpath
import scrapy
import json
import pickle

class SongsSpider(scrapy.Spider):
    name = 'songs'
    custom_settings = {
        "download_maxsize" : 0,
        "DOWNLOAD_WARNSIZE" : 0,
    }
    allowed_domains = ['hypergryph.com', 'hycdn.cn']
    start_urls = ['https://monster-siren.hypergryph.com/api/songs']

    def parse(self, response):
        """
        获取所有歌曲cid并拼接成链接发送
        :param response:
        :return:
        """

        try:
            with open("song_ids.pkl","rb") as file:
                song_ids = pickle.load(file)
        except FileNotFoundError:
            song_ids = set()

        link_id = jsonpath(json.loads(response.text), '$..cid')
        for link in link_id:
            if link in  song_ids:
                continue
            song_ids.add(link)
            url = 'https://monster-siren.hypergryph.com/api/song/' + link
            yield scrapy.Request(
                url=url,
                callback=self.music_url
            )
        with open("song_ids.pkl","wb") as file:
            pickle.dump(song_ids,file)
        
        try:
            with open("album_ids.pkl","rb") as file:
                album_ids = pickle.load(file)
        except FileNotFoundError:
            album_ids = set()

        album_id = jsonpath(json.loads(response.text), '$..albumCid')

        for album in album_id:

            if album in album_ids:
                continue
            album_ids.add(album)
            album_url = 'https://monster-siren.hypergryph.com/api/album/'+album+ '/data'
            # 发送请求，获取专辑封面
            yield scrapy.Request(
                url=album_url,
                callback=self.album_data,
                meta={'album_id':album}
            )
        with open("album_ids.pkl","wb") as file:
            pickle.dump(album_ids,file)
        
            
        pass

    def music_url(self, response):
        """
        解析链接内容获取歌曲名、歌词文件url、音频文件url
        :param response:
        :return:
        """
        cache = json.loads(response.text)
        album_id = jsonpath(cache, '$..albumCid')[0]
        source_url = jsonpath(cache, '$..sourceUrl')[0]
        suffix = source_url[-3:]
        name = jsonpath(cache, '$..name')[0]
        # 发送请求，获取音频文件
        yield scrapy.Request(
            url=source_url,
            callback=self.music_mp3,
            meta={'name': name,'album_id':album_id,'suffix' :suffix}
        )

        pass

    def music_mp3(self, response):
        """
        解析数据，发送给pipelines.py处理
        :param response:
        :return:
        """
        print(response.meta['name']+'.'+response.meta['suffix'])
        temp = MonsterSirenItem()
        temp['name'] = response.meta['name']
        temp['source'] = response.body
        temp['album_id'] = response.meta['album_id']
        temp['is_album'] = False
        temp['suffix'] = response.meta['suffix']
        yield temp
        pass

    def album_data(self, response):
        cache = json.loads(response.text)
        cover_url = jsonpath(cache,'$..coverUrl')[0]
        name = jsonpath(cache,'$..name')[0]
        yield scrapy.Request(
            url=cover_url,
            callback=self.album_jpg,
            meta={'name': name,'album_id':response.meta['album_id']}
        )
        pass

    def album_jpg(self, response):
        """
        解析数据，发送给pipelines.py处理
        :param response:
        :return:
        """
        print(response.meta['name']+'.jpg')
        temp = MonsterSirenItem()
        temp['name'] = response.meta['name']
        temp['source'] = response.body
        temp['album_id'] = response.meta['album_id']
        temp['is_album'] = True
        temp['suffix'] = 'jpg'
        yield temp
        pass
