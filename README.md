# Read this in [English](README_en.md)



# monster-siren-Scrapy

本项目使用Scrapy框架，爬取塞壬唱片官网所有歌曲文件。

## 基于
本项目受到 [FrothierNine346/scrapy-monster-siren](https://github.com/FrothierNine346/scrapy-monster-siren) 的启发，并在其基础上进行了改进和发展。我们感谢原作者提供的基础代码和灵感。

### 原始项目版权
原项目由 FrothierNine346 开发，并在 GNU General Public License v3.0 下发布。

### 许可证
与原始项目一致，本项目也遵循 GNU General Public License v3.0。

## 项目修改
本项目在原 `scrapy-monster-siren` 的基础上做了以下修改：
- 删除了下载歌词文件的功能
- 新增对wav格式无损音乐的支持
- 使用了新的文件结构，现在同一专辑的歌曲会放在同一文件夹下
- 新增唱片封面下载，方便后续转换格式，增添metadata等操作
- 使用pickle记录已经下载过的歌曲，避免重复爬取~~角应该不至于出1e6首歌吧~~
- ~~可能已经没用了但是没看懂的代码一律没删问就是我菜~~

## 使用方式
需要安装以下模块:
`scrapy`、`jsonpath`

在项目目录(monster_siren)运行:
```scrapy crawl songs```
运行爬虫