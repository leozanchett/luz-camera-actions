import yaml
import xml.etree.ElementTree as ET

def create_subtree_element(name: str, parent: ET.Element, data: dict, data_key: str = None):
   ET.SubElement(parent, name).text = data[data_key or name]

def create_href_element(name: str, parent: ET.Element, data: str):
   ET.SubElement(parent, name, {'href': data})

with open('feed.yaml') as f:
   yaml_data = yaml.safe_load(f)
   rss_element = ET.Element('rss', {'version': '2.0',
      'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
      'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'})

   channel_element = ET.SubElement(rss_element, 'channel')
   link_prefix = yaml_data['link']

   create_subtree_element('title', channel_element, yaml_data)
   create_subtree_element('format', channel_element, yaml_data)
   create_subtree_element('subtitle', channel_element, yaml_data)
   create_subtree_element('itunes:author', channel_element, yaml_data, 'author')
   create_subtree_element('description', channel_element, yaml_data)
   create_href_element('itunes:image', channel_element, link_prefix + yaml_data['image'])
   create_subtree_element('language', channel_element, yaml_data)
   create_subtree_element('link', channel_element, yaml_data)
   create_subtree_element('itunes:category', channel_element, yaml_data, 'category')

   for item in yaml_data['item']:
      item_element = ET.SubElement(channel_element, 'item')
      create_subtree_element('title', item_element, yaml_data)
      create_subtree_element('itunes:author', item_element, yaml_data, 'author')
      create_subtree_element('description', item_element, item)
      create_subtree_element('itunes:duration', item_element, item, 'duration')
      create_subtree_element('pubDate', item_element, item, 'published')
      create_subtree_element('title', item_element, item)
      enclosure_element = ET.SubElement(item_element, 'enclosure', {
         'url': link_prefix + item['file'],
         'length': item['length'],
         'type': 'audio/mpeg'
      })



   output_tree = ET.ElementTree(rss_element)
   output_tree.write('podcast.xml', encoding='utf-8', xml_declaration=True)
