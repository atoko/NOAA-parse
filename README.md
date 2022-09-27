# Publically available dataset parsing

## NOAA 

### `noaa-get-latest-rss.sh` 

Collects current information from NOAA's RSS feed (`data/rss/*`) and filters any nhc namespaced items into a stream of input events (`data/rss-nhc/*`), each separated by a newline character `\n`

The data is kept local to the filesystem and is organized by `{PREFIX}/year/month/day/timestamp`, where PREFIX is one of the directories wiithin the local folder `data`.

#### Requirements

This script attempts to be as self contained as possible within the python3 ecosystem. It creates a virtual python environment and installs packages from the pip repository. Please see `requirements.txt` for a list of dependencies


