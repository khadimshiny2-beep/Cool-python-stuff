# IP Collector

A tiny Python script that resolves a website's domain name to its IPv4 address.

## Requirements

| Requirement | Why it's needed |
|---|---|
| Python 3.10+ | Runs the script |
| Internet connection | Needed for the DNS lookup |

There are **no third-party packages** to install: the script only uses Python's built-in `socket` module, so no `requirements.txt` is needed.

## Usage

```bash
python ip_collector.py
```

```
Enter website URL: example.com
IP Adress : 93.184.216.34
```

Enter the **domain name only** (e.g. `example.com` or `www.example.com`). Do not include `https://` or any path, otherwise the lookup will fail.

## Troubleshooting

- **`socket.gaierror: [Errno -2] Name or service not known`**: the domain doesn't exist, has a typo, or you included `https://` / a trailing path. You are also possibly offline.
- Only an **IPv4** address is returned. Sites behind a CDN (e.g. Cloudflare) return the CDN's IP, not the origin server's.

## Legal notice

For personal and educational use. Only look up addresses for lawful purposes.