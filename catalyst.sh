#!/bin/bash

# make a directory with today's date if it does not exist
DATE=$(date -u +%Y-%m-%d);
if [ ! -d ".//catalyst_snapshot//$DATE" ]; then
    echo "Creating ./catalyst_snapshot/$DATE to store parcel data";
    mkdir ".//catalyst_snapshot//$DATE";
fi

# get coordinates.txt file from command line or use default
COORD_FILE=$1;
if [ -z "$COORD_FILE" ]; then
    COORD_FILE="coordinates.txt";
    echo "Using ./coordinates.txt as the coordinate file";

    if [ ! -f "$COORD_FILE" ]; then
        echo "./coordinates.txt does not exist, please specify a file containing coordinates to download data.";
        exit;
    fi
fi

while read -r LINE; do
  mkdir ".//catalyst_snapshot//$DATE//parcel_$LINE"
  curl "https://peer.decentraland.org/content/entities/scene?pointer=$LINE" \
  | jq -r ".[0].content[]|[.file, .hash] | @csv" \
  | while IFS="," read -r pat url; do
    # remove double quotes from prefix and suffix
    temppat=$(sed -e 's/^"//' -e 's/"$//' <<<$pat);
    tempurl=$(sed -e 's/^"//' -e 's/"$//' <<<$url);

    url3="https://peer.decentraland.org/lambdas/contentv2/contents/$tempurl";

    if [ ! -f ".//catalyst_snapshot//$DATE//parcel_$LINE//$temppat" ]; then
        curl --create-dirs -o ".//catalyst_snapshot//$DATE//parcel_$LINE//$temppat" $url3;
    fi
  done
done < $COORD_FILE