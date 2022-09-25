# Requirements
python3 -m venv .venv

./.venv/bin/pip3 install -r requirements.txt --require-virtualenv
mkdir -p ./noaa

# Extract
export year=$(date +%y)
export month=$(date +%m)
export day=$(date +%d)
export timestamp=$(date +%s)

mkdir -p ./noaa/rss/"${year}"/"${month}"/"${day}"/
curl https://www.nhc.noaa.gov/gis-at.xml > ./noaa/rss/"${year}"/"${month}"/"${day}"/"${timestamp}"

# Transform
mkdir -p ./noaa/rss-nhc/"${year}"/"${month}"/"${day}"/
./.venv/bin/python3 ./noaa-rss-nhc.py ${year} ${month} ${day} ${timestamp}