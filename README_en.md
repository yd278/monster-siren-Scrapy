[中文版](README.md)

# monster-siren-Scrapy

This project utilizes the Scrapy framework to crawl and download all song files from the Monster-Siren Records official website.

## Based On
This project is inspired by [FrothierNine346/scrapy-monster-siren](https://github.com/FrothierNine346/scrapy-monster-siren) and has been improved and developed based on it. We thank the original author for providing the foundational code and inspiration.

### Original Project Copyright
The original project was developed by FrothierNine346 and is released under the GNU General Public License v3.0.

### License
Consistent with the original project, this project also adheres to the GNU General Public License v3.0.

## Project Modifications
This project has made the following modifications on the basis of the original `scrapy-monster-siren`:
- Removed the functionality to download lyric files.
- Added support for downloading music in WAV format.
- Implemented a new file structure, where songs from the same album are now stored in the same folder.
- Added functionality to download album covers, which facilitates subsequent format conversion and adding of metadata.
- ~~Left some mysterious code untouched because, let's face it, sometimes you just tweak what you need and roll with it. Call it the art of pragmatic coding!~~

## How to Use
You need to install the following modules:
`scrapy`, `jsonpath`

Run the following command in the project directory (monster_siren):
```scrapy crawl songs```
to run the spider.
