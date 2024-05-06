# <p align="center" width="100px" heigth="100px">![](img/banner.png)</p>

## Install

### Via pipx
```sh
pipx install git+https://github.com/phor3nsic/destiny
```

### Via source
```sh
git clone https://github.com/phor3nsic/destiny \
&& cd destiny \
pip install .
```

## Run

### List of Hosts
```sh
cat hosts.txt | destiny
```

### Tool integrations

_For Subdomains:_

```sh
subfinder -d hackerone.com -silent | destiny
```

_For vhosts:_
```sh
subfinder -d hackerone.com -silent | httpx -vhost -silent| grep vhost| awk -F ' ' '{print $1}'| awk -F 'https://' '{print $2}'| destiny
```