<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0e0424&height=130&section=header&text=GitHub-WebScrapping&fontSize=39&fontColor=fff&animation=twinkling&fontAlignY=35"/> 

<div align="center"> 
<p>Technologies used:</p>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Linux-1e1f20?style=for-the-badge&logo=linux&logoColor=yellow"></a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Qt-052F15?style=for-the-badge&logo=qt&logoColor=green"></a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Python-141b4a?style=for-the-badge&logo=python&logoColor=green"></a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Bash-082405?style=for-the-badge&logo=gnu bash&logoColor=white"></a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Css-024550?style=for-the-badge&logo=css3&logoColor=cyan"></a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Git-161618?style=for-the-badge&logo=git&logoColor=orange"></a>
</div>


<div align="center">
<h1>github-webscrapping
</div>
<div align="center">
<img src="./icons/github-webscrapping.svg" width="100">
</div>

**GitHub Web Scraping** is a utility developed in **Python** and **Qt** that utilizes various modules to make web queries and retrieve information about GitHub profile repositories, as well as details about the profile in question. It features functionalities that allow you to save performed queries and clone repositories from within the same application.

<div align="center">
<p>github-webscrapping
</div>

![1](./screenshots/Screenshot_1.png?raw=true)

## Install via deb package
To install github-webscrapping, you will first need to download the **Debian package**, which can be found at the following link: 

<a href="https://github.com/TheWatcherMultiversal/github-webscrapping/releases/download/v1.0.1/github-webscrapping_1.0.1_all.deb" target="_blank">📦 Download deb package</a>

Once we have our **Debian package** installed, simply execute the following command, and it will be downloaded to our system:

    sudo dpkg -i github-webscrapping_1.0.1_all.deb
    
- Note: If we find any missing dependencies, it's just a matter of installing them with the `sudo apt install -f` command

Now we just need to check if the program was installed correctly, for this we execute the following:

    github-webscrapping

## Install using a script
If you do not have a Debian-based distribution or if you have a different package manager, you can use the installation script `./install.py`.

To do this, first make sure that the `./install.py` script and the `./uninstall.py` script have the necessary permissions to run on the system:

    chmod 755 ./install.py ./uninstall.py

Now we can install github-webscrapping by running the installation script:

    ./install.py

- Note: You can uninstall github-webscrapping from the system using the `./uninstall.py` script.

Now we just need to check if the program was installed correctly, for this we execute the following:

    github-webscrapping

In case you encounter any errors while running the script, please read the error messages provided by the script. Additionally, you will need to install the necessary dependencies to run github-webscrapping correctly.

## Dependencies
Before being able to use github-webscrapping, you need to have the following **dependencies** installed on your system for the program to function properly:

- **python3-requests**
- **python3-bs4**
- **python3-pyqt5**
- **python3-lxml**
- **qtbase5-dev**

## Report bugs or give suggestions
To notify errors in the program or give suggestions for it, write your request in the following email: <universepenguin@protonmail.com>
