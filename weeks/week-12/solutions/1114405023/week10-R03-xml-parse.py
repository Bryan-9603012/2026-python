import xml.etree.ElementTree as ET
xml_data = '\n<rss version="2.0">\n  <channel>\n    <title>Planet Python</title>\n    <item>\n      <title>討論 Python 型別提示</title>\n      <link>https://example.com/1</link>\n      <author>Alice</author>\n    </item>\n    <item>\n      <title>asyncio 最佳實踐</title>\n      <link>https://example.com/2</link>\n      <author>Bob</author>\n    </item>\n  </channel>\n</rss>\n'
root = ET.fromstring(xml_data)
print('根標籤：', root.tag)
print('屬性：', root.attrib)
channel = root.find('channel')
print('頻道名稱：', channel.find('title').text)
for item in root.findall('channel/item'):
    title = item.find('title').text
    author = item.find('author').text
    print(f'  [{author}] {title}')
print('\n所有 <title>：')
for elem in root.iter('title'):
    print(' ', elem.text)
version = root.get('version')
print('\nRSS 版本：', version)
print('不存在的屬性：', root.get('missing', '預設值'))
