import sys
import xml.etree.ElementTree
import re

year = sys.argv[1]
month = sys.argv[2]
day = sys.argv[3]
timestamp = sys.argv[4]

raw_xml = open(f"""./noaa/{year}/{month}/{day}/{timestamp}""").read()
tag_start = raw_xml.find("<nhc:Cyclone>")
tag_end = raw_xml.find("</nhc:Cyclone>")
tag_data = raw_xml[tag_start:tag_end+len("</nhc:Cyclone>")]
tag_data = tag_data.replace("nhc:", "")
# TODO: implement XMLParser and ignore elements other than <nhc:Cyclone>
parsed = xml.etree.ElementTree.fromstring(tag_data)

dt = parsed.find("datetime").text
name = parsed.find("name").text

if __name__ == "__main__":
    print(f"""
        Cyclone data:
            name: {name} 
            date: {dt}
        """)
