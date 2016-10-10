# Light Block Explorer for Zcash (LBE-Zcash)

- __Author__: Ondrej Sika <ondrej@ondrejsika.com>
- __License__: MIT <http://ondrejsika.com/license/mit.txt>


### Abstract

Basic block explorer for Zcash

### Xcoind requirements

LBE requires this rpc calls:

- getbestblockhash
- getblock
- getrawtransaction
- decoderawtransaction


### Install

    git clone git@github.com:ondrejsika/lbe-zcash.git
    cd lbe-zcash
    virtualenv .env
    source .env/bin/activate
    pip install -r requirements.txt


### Usage

Show help

    python lbe.py -h

