export year=$(date +%y)
export month=$(date +%m)
export day=$(date +%d)
export timestamp=$(date +%s)

mkdir -p ./noaa/"${year}"/"${month}"/"${day}"/
curl https://www.nhc.noaa.gov/gis-at.xml > ./noaa/"${year}"/"${month}"/"${day}"/"${timestamp}"
python3 ./parse-noaa.py ${year} ${month} ${day} ${timestamp}

