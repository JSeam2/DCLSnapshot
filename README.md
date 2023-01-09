# Decentraland Snapshot Tool

Creates a snapshot of all decentraland spaces

## Quickstart
There are two snapshot flows available. TheGraph Snapshot captures only onchain information. Catalyst Snapshot captures the parcel information stored within the Catalyst peer nodes used by Decentraland. Catalyst is the content server used by Decentraland. GLTFs and other parcel data is not stored on-chain but off-chain via Catalyst. [See the repo for Catalyst](https://github.com/decentraland/catalyst)

### TheGraph Snapshot
This will create a snapshot across the various parcels indexed by TheGraph.

1. The project uses pipenv for dependency management. [Make sure you install pipenv first.](https://pipenv.pypa.io/en/latest/)

2. Obtain an API key from [Thegraph](https://thegraph.com). Copy `secret.py.example` into `secret.py` and replace the key.

3. Install all packages from the Pipfile
```shell
pipenv install
```

4. Activate the pipenv environment
```shell
pipenv shell
```

5. Run the script. The script will create folders within `./thegraph_snapshot` followng this structure `./thegraph_snapshot/<unixtimetamp>/estate_<estateId>` or `./snapshot/<unixtimestamp>/tokenId_<tokenId>`  and then store the various dcl parcel information within them.
```shell
python thegraph.py
```

6. Within the folder a `metadata_<tokenId>.json` (or multiple in the case of estates) will be stored containing the following information obtained from Thegraph.
```json
      {
        "id": "parcel-0xf87e31492faf9a91b02ee0deaad50d51d56d5d4d-0",
        "tokenId": "0",
        "owner": {
          "id": "0x959e104e1a4db6317fa58f8295f586e1a978c297",
          "address": "0x959e104e1a4db6317fa58f8295f586e1a978c297"
        },
        "x": "0",
        "y": "0",
        "data": {
          "id": "parcel-0xf87e31492faf9a91b02ee0deaad50d51d56d5d4d-0",
          "ipns": "ipns:QmQUXM5vQKBf715uzLYwK5tfo5RigvVerEYuoFdmNN3Fu1",
          "name": "",
          "description": "",
          "version": "0"
        },
        "estate": {
          "id": "estate-0x959e104e1a4db6317fa58f8295f586e1a978c297-1164",
          "tokenId": "1164",
          "size": 380
        }
      }
```

### Catalyst Server Snapshot
This will store the various GLTFs stored within the Catalyst content server.
It uses the endpoint provided by Decentraland to download parcel content.

1. Obtain the coordinates you want to download. Store it within the root of the repository as `coordinates.txt`.
If not you can pass the file as an argument to the bash script.
The coordinates file should look like this.
```
-150,-11
-150,-12
-150,-13
-150,-130
-150,-132
-150,-136
-150,-137
-150,-138

... so on
```

2. Run the bash script as follows. It will create a date `YYYY-MM-DD` folder as follows `catalyst_snapshot/YYYY-MM-DD`.
The script will then download parcel information and store the data within separate folders within the folder as `parcel_-150,-123`.
```shell
# if you are using the default coordinates.txt file
$ bash catalyst.sh

# if you want to specify a file
$ bash catalyst.sh chunk_1.txt
```

## Additional Configurations

### ipfs_gateway.py

IPFS gateways are not used, but this file is kept for reference. DCL stores the assets within their Catalyst content server and not IPFS. Only the addressing scheme for IPFS is used.

~~A list of public IPFS gateways have already been included in `./ipfs_gateway.py`.~~
~~You may need to modify them should the gateways go down.~~
~~Multiple public gateways are used to prevent rate throttling by a single gateway.~~