# Publically available dataset parsing

## NOAA 

### `noaa.sh` 

Collects current information from NOAA's RSS feed (`noaa/rss/*`) and filters any nhc namespaced items into a stream of input events (`noaa/rss-nhc/*`), each separated by a newline character `\n`

The data is kept local to the filesystem and is organized by `{PREFIX}/year/month/day/timestamp`, where PREFIX is one of the directories wiithin the local folder `noaa`.

#### Requirements

`noaa.sh` attemtps to be as self contained as possible within the python3 ecosystem. It will attempt to create a virtual python environment and install packages from the pip repository. 


