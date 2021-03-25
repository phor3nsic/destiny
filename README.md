# <p align="center" width="100px" heigth="100px">![](imgs/banner.png)</p>

### RUN

> Clone
```
git clone https://github.com/phor3nsic/Destiny.git
```
> Install requirements

```
cd Destiny && pip3 install -r requirements.txt
```

> Simple Run
```
cat hosts.txt | python3 destiny.py
```

> Tool integrations

_For Subdomains:_

```
subfinder -d hackerone.com -silent | python3 destiny.py
```

_For vhosts:_
```
subfinder -d hackerone.com -silent | httpx -vhost -silent| grep vhost| awk -F ' ' '{print $1}'| awk -F 'https://' '{print $2}'| python destiny.py
```


