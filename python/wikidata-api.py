#!/usr/bin/env python
#
#
"""
Documentation
- https://www.mediawiki.org/wiki/API:Main_page
- Wiktionary: http://en.wiktionary.org/w/api.php
- API Query Action: https://www.mediawiki.org/wiki/API:Query
- API Sandbox: http://en.wiktionary.org/wiki/Special:ApiSandbox
"""

import urllib
import datetime
import simplejson as json

# Timestamp
utc_datetime0 = datetime.datetime.utcnow()
time_now = utc_datetime0.strftime("%Y-%m-%d_%H-%M-%S")  # or ("%Y-%m-%d %H:%M:%S")

# Paths
osx = '/Users/'
win = 'C:\\'


# URL ENDPOINT
# Endpoint page displays useful documentation links. Adjust en. to respective ISO language code
# URL endpoint will often be easy to determine: 'http://en.wikipedia.org/w/api.php'

url_sample = \
    'http://en.wikipedia.org/w/api.php?format=json&action=query&titles=Main%20Page&prop=revisions&rvprop=content'

url_endpoint = 'http://en.wiktionary.org/w/api.php'

# User-Agent
# user-agent header must include metadata information for queries to work
headers = {
    'User-Agent': 'WiktionaryData/0.9'
    # DocExample: MyCoolTool/1.1 (http://example.com/MyCoolTool/; MyCoolTool@example.com) BasedOnSuperLib/1.4
}

# Action:Query module
# largely composed 3 sub-modules
action = 'query'

# Targeting Wiki items
# Batch many requests via '|' e.g. 'titles=PageA|PageB|PageC'
titles = ''

pageids = ''

revids = ''

params_input = {
    'titles': titles,
    'pageids': pageids,
    'revids': revids,
}


revisions = 'revisions'  # Set as 'revisions' by default will return most recent revision

# Continue parameter must be used for pagination purposes (https://www.mediawiki.org/wiki/API:Query)
pagination = ''

params_all = {
    'format': 'json',  # Keep as json. jsonfm = pretty-printed HTML
    'action': action,  # Batch many requests via '|'
    'prop': revisions,
    'continue': pagination,
}
params_all.update(params_input)


# Functions


def run():
    url_api = url_endpoint + '?' + urllib.urlencode(params_all)
    response = json.loads(urllib.urlopen(url_api).read())

    pretty_response = json.dumps(response, ensure_ascii=False, encoding='utf-8')
    print pretty_response







# Sandbox Results

# Tried: titles='internet'
"""
{
    "query": {
        "pages": {
            "176887": {
                "pageid": 176887,
                "ns": 0,
                "title": "internet"
            }
        }
    }
}

"""


