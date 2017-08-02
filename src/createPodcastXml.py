# coding: utf-8

import os,os.path
import time
import datetime

import glob

ABE_NAME = 'BeyondTheAverage'
GARAGE_NAME = 'PeteGarage'
FILE_PATH = "."


def create_xml_header():
	xml = '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<rss xmlns:itunes=\"http://www.itunes.com/dtds/podcast-1.0.dtd\" version=\"2.0\">
<channel>
	<title>{CAST_TITLE}</title>
	<link>{CAST_LINK}</link>
	<language>{CAST_LANGUAGE}</language>
	<copyright>{CAST_COPYRIGHT}</copyright>
	<itunes:subtitle>{CAST_SUBTITLE}</itunes:subtitle>
    <itunes:author>{ITUNES_AUTHOR}</itunes:author>
	<itunes:summary>{ITUNES_SUMMARY}</itunes:summary>
	<description>{CAST_DESCRIPTION}</description>
	<itunes:owner>
		<itunes:name>{ITUNES_OWNER_NAME}</itunes:name>
		<itunes:email>{ITUNES_OWNER_EMAIL}</itunes:email>
	</itunes:owner>
	<itunes:image href={ITUNES_IMAGE}/>
	<image>
		<url>{CAST_IMAGE_URL}</url>
		<title>{CAST_IMAGE_TILTE}</title>
        <link>{CAST_IMAGE_LINK}</link>
	</image>
	<pubDate>{CAST_PUBDATE}</pubDate>
    <itunes:explicit>{ITUNE_EXPLICIT}</itunes:explicit>'''\
.format(CAST_TITLE='NISSAN あ、安部礼司 ～ BEYOND THE AVERAGE ～ - TOKYO FM',
	CAST_LINK='http://raspberrypi.local/radiko/',
	CAST_LANGUAGE='ja',
	CAST_COPYRIGHT='Copyright(c) 2015 TOKYO FM All Rights Reserved.',
	CAST_SUBTITLE='【毎週日曜17:00更新】',
	ITUNES_AUTHOR='TOKYO FM',
	ITUNES_SUMMARY='番組の舞台は、東京・神田神保町にある中堅企業「大日本ジェネラル」で、ここに勤務する平均的男性社員・安部礼司の会社内外でのストーリーを中心に展開される',
	CAST_DESCRIPTION='基本的には、安部が一週間の出来事を語る内容となっており、番組の最後に安部が自宅でブログを更新するシーンで締めるのが通例である。（なお、このブログにて重大発表が行なわれる場合もある）。',
	ITUNES_OWNER_NAME='TOKYO FM',
	ITUNES_OWNER_EMAIL='podcasts@tfm.co.jp',
	ITUNES_IMAGE='\"http://raspberrypi.local/radiko/abe_photo.jpg\"',
	CAST_IMAGE_URL='http://raspberrypi.local/radiko/abe_photo_300x300.jpg',
	CAST_IMAGE_TILTE='NISSAN あ、安部礼司 ～ BEYOND THE AVERAGE ～ - TOKYO FM',
	CAST_IMAGE_LINK='http://raspberrypi.local/radiko/',
	CAST_PUBDATE='Sat, 20 May 2017 17:50:00 +0900',
	ITUNE_EXPLICIT='clean')
	return xml

def create_xml_item(title, author, subtitle, summary, url, length, type, guid, pubDate, duration, link, description):
	xml = '''<item>
	<title>{ITEM_TITLE}</title>
	<itunes:author>{ITEM_AUTHOR}</itunes:author>
	<itunes:subtitle>{ITEM_SUBTITLE}</itunes:subtitle>
	<itunes:summary>{ITEM_SUMMARY}</itunes:summary>
	<enclosure url={ITEM_URL} length={ITEM_LENGTH} type={ITEM_TYPE} />
	<guid>{ITEM_GUID}</guid>
	<pubDate>{ITEM_PUBDATE}</pubDate>
	<itunes:duration>{ITEM_DURATION}</itunes:duration>
	<link>{ITEM_LINK}</link>
	<description>{ITEM_DESCRIPTION}</description>
</item>'''.format(ITEM_TITLE= title, ITEM_AUTHOR= author, ITEM_SUBTITLE= subtitle, ITEM_SUMMARY= summary, ITEM_URL= url, ITEM_LENGTH=length, ITEM_TYPE=type, ITEM_GUID=guid, ITEM_PUBDATE=pubDate, ITEM_DURATION=duration, ITEM_LINK=link, ITEM_DESCRIPTION=description)
	return xml



def create_xml_items(dir_path, base_url):
	files = glob.glob(dir_path + '*.mp3')
	print files
	#files.sort(key=os.path.getmtime, reverse=False)
#mtime = datetime.datetime.fromtimestamp(os.stat('./BeyondTheAverage_20170604.mp3').st_mtime)
#print mtime.weekday()
#YMD = mtime.strftime('%Y/%m/%d')
#print YMD
#
#for file in files:
#    print file
#
#files = os.listdir(".")
#files.sort(key=os.path.getmtime, reverse=False)
#for i, file_path in enumerate(files):
#    print("{} {}".format(i, file_path))
#    if file_path.endswith("mp3"):
#        date = datetime.datetime.fromtimestamp(os.stat(file_path).st_mtime)
#        pre_fix = date.strftime('%Y%m%d')
#        # Sat
#        if date.weekday() == 5:
#            new_name = GARAGE_NAME + '_' + pre_fix
#        # Sun
#        elif date.weekday() == 6:
#            new_name = ABE_NAME + '_' + pre_fix
#        print new_name
#        os.rename(file_path, new_name)

#TEST = '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
#<rss xmlns:itunes=\"http://www.itunes.com/dtds/podcast-1.0.dtd\" version=\"2.0\">
#<channel><title>{}<\/title>
#hello'''.format('NISSAN あ、安部礼司 ～ BEYOND THE AVERAGE ～ - TOKYO FM')

xml_header = create_xml_header()
xml_footer = '</channel>\n</rss>'

create_xml_items('.', 'http://raspberrypi.local/radiko/')

print create_xml_item('2017/05/21 安部礼司', '安部礼司', '2017/05/21', 'さまり', '\"http://raspberrypi.local/radiko/abe_20170521.mp3\"', '\"57601674\"', '\"audio/mpeg\"', 'http://raspberrypi.local/radiko/abe_20170521.mp3', 'Sat, 21 May 2017 17:00:00 +0900', '00:60:00', 'http://raspberrypi.local/radiko/', '2017/05/21')

print xml_header
print xml_footer

