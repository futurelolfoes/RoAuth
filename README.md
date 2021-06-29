# RoAuth 
### An easier, open-sourced way to authenticate ownership of roblox accounts.
![GitHub repo size](https://img.shields.io/github/repo-size/n0vuh/RoAuth?style=flat-square) ![GitHub](https://img.shields.io/github/license/n0vuh/RoAuth?style=flat-square) ![GitHub Repo stars](https://img.shields.io/github/stars/n0vuh/RoAuth?style=flat-square) ![GitHub last commit](https://img.shields.io/github/last-commit/n0vuh/RoAuth?style=flat-square)

---

**Does this work with the latest ROBLOX update?**
Yes, it does.

**How does it work?**
RoAuth uses aiohttp & asyncio to make non-blocking requests to retrieve user information via ROBLOX's api. RoAuth generates keys by getting a random choice of words from words.txt, then checks to see if the end user has made that their description. If they have in the alotted time, it will change their username to their ROBLOX account name.

---

**Dependencies**
* Python 3.8>
* json
* aiohttp
* asyncio
* discord.py
* nest_asyncio
* random
