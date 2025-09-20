# ygygi67-MWN
สามารถใน termux ได้
โค้ดสามารถดึงรูปนักเรียน คุณครู และบัตรนักเรียน จากทั้งระบบออกมาได้


## Features
- ดึงรูปนักเรียนจากทั้งระบบได้ จากโค้ด images.py
- ดึงรูปคุณครูจากทั้งระบบได้ จากโค้ด teachers.py
- ดึงบัตรนักเรียนจากทั้งระบบได้ (อัตรายอาจโดยแบบ IP และทำให้ระบบหน่องและค้างได้) จากโค้ด key.py

### ผู้ที่จะเริ่มใช้โค้ดให้ใส่คำสั่งมานี้
```bash
pkg update -y && pkg upgrade -y
```
```bash
pkg install -y python
```
```bash
pkg install -y python python2 ruby php nodejs git curl wget nano unzip zip tmux vim openssl-tool nmap net-tools dnsutils socat proot figlet toilet
```
```bash
pkg install -y x11-repo root-repo unstable-repo
```
```bash
pkg install -y tigervnc x11-utils xterm
```
```bash
pkg install -y termux-api
```
```bash
gem install lolcat
```
```bash
pip install --upgrade pip
pip install requests colorama bs4 mechanize
```
```bash
git clone https://github.com/ygygi67/ygygi67-MWN/
```
```bash
cd ygygi67-MWN
```
```bash
pip install -r requirements.txt
```
มาถึงตรงนี้สามารถรันโค้ดที่มีให้ตามใจชอบ เช่น
```bash
python key.py
```

## วิธีลบไฟล์ใน Termux (remove)
- ``` rm ``` ตามด้วยชื่อไฟล์
- ```rm -r```  ตามด้วยชื่อโฟลเดอร์
- ```rm -rf``` เพื่อลบโฟลเดอร์พร้อมเนื้อหาแบบบังคับโดยไม่ถามยืนยัน
### แค่อยากใส่มาเดียวมาแก้

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Build](https://img.shields.io/badge/build-passing-brightgreen)


## Demo
![screenshot](https://cdn.discordapp.com/attachments/1300061288621277296/1418786346922803342/image.png?ex=68cf6340&is=68ce11c0&hm=aa689ffadaeb7fa4f85725079537a9de9b2ea6abc99e36acb471d96a3e5ebcb7&)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- [x] ดึงรูปหน้าที่คนในโรงเรียน
- [x] ดึงรูปครูทุกคนในโรงเรียน
- [x] หารหัสนักเรียน
- [x] ทำเว็บโรงเรียนค้างได้
- [ ] ดึงบัตรนักเรียนออกมาได้
- [ ] หารหัสผ่านทุกคนในโรงเรียน

## Contributors
- [@ygygi67](https://github.com/ygygi67) - Developer
- [@ygygi67](https://www.youtube.com/channel/UCmv8yCHA_JxyY2EsmBcveWA/) - Youtube
