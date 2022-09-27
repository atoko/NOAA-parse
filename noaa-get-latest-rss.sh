# Requirements
python3 -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt --require-virtualenv
mkdir -p ./data

export YEAR=$(date +%y)
export MONTH=$(date +%m)
export DAY=$(date +%d)
export TIMESTAMP=$(date +%s)


# Extract
export EXTRACT_ROOT="data/rss"
mkdir -p ./noaa/"${EXTRACT_ROOT}"/"${YEAR}"/"${MONTH}"/"${DAY}"/
curl https://www.nhc.noaa.gov/gis-at.xml > ./noaa/"${EXTRACT_ROOT}"/"${YEAR}"/"${MONTH}"/"${DAY}"/"${TIMESTAMP}"

# Transform
export TRANSFORM_ROOT="data/rss-nhc"
mkdir -p ./noaa/"${TRANSFORM_ROOT}"/"${YEAR}"/"${MONTH}"/"${DAY}"/
python3 noaa-get-latest-rss.py ${EXTRACT_ROOT} ${TRANSFORM_ROOT} ${YEAR} ${MONTH} ${DAY} ${TIMESTAMP}