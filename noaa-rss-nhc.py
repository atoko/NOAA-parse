import json
import sys
import time
from uuid import uuid4

import bs4
from bs4 import BeautifulSoup

year = sys.argv[1]
month = sys.argv[2]
day = sys.argv[3]
timestamp = sys.argv[4]

span = uuid4()

def within_nhc_namespace(tag: bs4.Tag):
    return tag.prefix == "nhc" and tag.parent.prefix is None

if __name__ == "__main__":
    input_path = f"""./noaa/rss/{year}/{month}/{day}/{timestamp}"""
    output_path = f"""./noaa/rss-nhc/{year}/{month}/{day}/{timestamp}"""

    print(json.dumps({
       'event': f"""noaa/parse_rss/open/{span}""",
       'timestamp': int(time.time()),
       'input_path': input_path,
    }))

    try:
        with open(input_path) as input_file:
            feed = BeautifulSoup(input_file, "xml")
            nhc_items = feed.find_all(within_nhc_namespace)

            if len(nhc_items) > 0:
                with open(output_path, 'w') as output_file:
                    for item in nhc_items:
                        xml = str(item).replace('\t', '')
                        xml = xml.replace('\n', '')
                        xml = xml.replace('\r', '')

                        output_file.write(xml)
                        output_file.write("\n")

                print(json.dumps({
                   'event': f"""noaa/parse_rss/write/{span}""",
                   'timestamp': int(time.time()),
                   'output_path': output_path,
                   'nhc_items': len(nhc_items)
                }))
    except RuntimeError as error:
        print(json.dumps({
            'event': f"""noaa/parse_rss/{span}""",
            'timestamp': int(time.time()),
            'message': error
        }, file=sys.stderr))