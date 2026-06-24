<h1 align="center">
  Destiny 🔮
  <br>
</h1>

<h4 align="center">Identify destiny of domain name</h4>

<h6 align="center"> Coded with 💙 by ph0r3nsic </h6>

<p align="center">

<br>
  <!--Tweet button-->
  <a href="https://twitter.com/intent/tweet?text=destiny%20-%20Identify%20destiny%20of%20domain%20name%20https%3A%2F%2Fgithub.com%2Fphor3nsic%2Fdestiny%20%23bash%20%23github%20%23linux%20%23infosec%20%23bugbounty" target="_blank">Share on Twitter!
  </a>
</p>

About 🔮
----------

`destiny` reads a list of hostnames from stdin, resolves each one to its IP
address (A record), and groups the hosts by the IP they point to. It's handy
during recon for spotting which subdomains share infrastructure.

Install 📡
----------

### Via pipx
```sh
pipx install git+https://github.com/phor3nsic/destiny
```

### Via source
```sh
git clone https://github.com/phor3nsic/destiny \
&& cd destiny \
&& pip install .
```

Examples 💡
----------
### List of Hosts
```sh
cat hosts.txt | destiny
```

### Tool integrations

_For Subdomains:_
- [subfinder](https://github.com/projectdiscovery/subfinder)

```sh
subfinder -d hackerone.com -silent | destiny
```

_For vhosts:_
- [subfinder](https://github.com/projectdiscovery/subfinder)
- [httpx](https://github.com/projectdiscovery/httpx)
```sh
subfinder -d hackerone.com -silent | httpx -vhost -silent| grep vhost| awk -F ' ' '{print $1}'| awk -F 'https://' '{print $2}'| destiny
```