[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)
[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)

# Linkedin Automation:

Uses: Scrapy, Selenium web driver, Chromium headless, docker and python3.

#### Linkedin Networking:
Python code to automatically expand your LinkedIn network based on your interest

#### Companies Code:
This code will send a message to all your new connections  on linkedin.
1. It goes to your possible connection;
2. Clicks on "Conecction" button;
3. Click on "Add Note"
4.- Type custome_message
5.- Make connection


### Install
Needed:
- webdriver-manager;
- selenium;
- python3.6;
- virtualenvs;


###### 1. Set up Linkedin login and password:
 - Open parameters.py file and provide your email id, password, and keywords for search criteria.


###### 2. Run and test :
 - Run `python linkedIn.py`



###### Test & Development:
Setup your python virtual environment (trivial but mandatory):

```bash
    virtualenvs -p python3.6 .venv
    source .venv/bin/activate
    pip install -r requirements.txt
```

Create the selenium server, open the VNC window and launch the tests, type those in three different terminals on the project folder:
```bash
    make dev
    make view
    make tests
```
## Screenshot

<img src="https://github.com/pseudo-r/LinkedinAutoMessage/blob/main/screenshot/search_parameter.png?raw=true" width="500" />
<img src="https://github.com/pseudo-r/LinkedinAutoMessage/blob/main/screenshot/connection.png?raw=true" width="500" />
<img src="https://github.com/pseudo-r/LinkedinAutoMessage/blob/main/screenshot/message.png?raw=true" width="500" />

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Legal

This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by Linkedin or any of its affiliates or subsidiaries. This is an independent and unofficial project. Use at your own risk.
This project violates Linkedin's User Agreement Section 8.2, and because of this, Linkedin may (and will) temporarily or permantly ban your account. We are not responsible for your account being banned.

