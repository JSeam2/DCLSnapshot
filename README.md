# Decentraland Snapshot Tool

Creates a snapshot of all decentraland spaces

## Quickstart
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

5. Run the script. The script will create folders within `./snapshot` followng this structure `./snapshot/<unixtimetamp>/<tokenId_estateTokenIdIfExists>` and then store the various dcl parcel information within them.
```shell
python main.py
```

6. Within the folder a `metadata.json` will be stored containing the following information obtained from Thegraph.
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

## Additional Configurations

### ipfs_gateway.py

A list of public IPFS gateways have already been included in `./ipfs_gateway.py`.
You may need to modify them should the gateways go down.
Multiple public gateways are used to prevent rate throttling by a single gateway.