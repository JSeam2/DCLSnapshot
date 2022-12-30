import requests
import ipfs_gateway
import secret
import logging
import sys
import json
import os
import time

# TODO: Graph mainnet doesn't seem to work
# DCL_GRAPH_ENDPOINT = f"https://gateway.thegraph.com/api/{secret.THEGRAPH_API_KEY}/id/GnwyhKp8uQkktC3vgMxWpg9f9qea75WQ6GXTxjW6BbZq"
# TODO: Hosted endpoint is limited to first (0-1000), skip (0-5000)
DCL_GRAPH_ENDPOINT = "https://api.thegraph.com/subgraphs/name/decentraland/marketplace"
DCL_CONTENT_SERVER = "https://peer.decentraland.org/content/contents/"

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')


stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('snapshot.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


def graph_query(first, skip):
    query = """
    {{
        parcels(first: {}, skip: {}, orderBy: tokenId) {{
        id
        tokenId
        owner {{
          id
          address
        }}
        x
        y
        data {{
          id
          ipns
          name
          description
          version
        }}
        estate {{
          id
          tokenId
          size
          rawData
        }}
      }}
    }}
    """.format(first, skip)

    response = requests.post(
        url=DCL_GRAPH_ENDPOINT,
        json={"query": query}
    )

    if response.status_code == 200:
        return json.loads(response.content)

    else:
        logger.error("Query failed at skip={}".format(skip))
        return None

def main():
    skip = 0
    first = 10

    # make base path with current time
    unixtime = str(int(time.time()))
    path = os.path.join("snapshot", unixtime)
    os.mkdir(path)

    while True:
        # Query the graph
        data = graph_query(first, skip)
        parcel_list = data["data"]["parcels"]

        # stop loop if there's no more parcel to index
        if len(parcel_list) == 0:
            break

        for parcel in parcel_list:
            print(parcel)
            # Save metadata in a subpath
            if parcel["estate"] is not None:
                subpath = os.path.join(path, parcel["tokenId"] + "_" + parcel["estate"]["tokenId"])
            else:
                subpath = os.path.join(path, parcel["tokenId"])

            os.mkdir(subpath)

            with open(os.path.join(subpath, "metadata.json"), "w") as f:
                json.dump(parcel, f, indent=2)

            # TODO: Look for the gltfs and save it within the folders

        skip += first


if __name__ == "__main__":
    main()