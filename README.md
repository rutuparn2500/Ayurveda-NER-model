Steps to Run the Project on Windows
1. Download the Project from GitHub
Option 1 : Using ZIP File
1.	Open the GitHub repository.
2.	Click Code : Download ZIP.
3.	Extract the ZIP file.
4.	Open the extracted folder.
Option 2 : Using Git
Open PowerShell or Command Prompt and run:
git clone <GITHUB_REPOSITORY_LINK>
Then go inside the project folder:
cd Ayurveda-NER-model-main\SattvaX

2. Open Terminal in Project Folder
Inside the SattvaX folder:
1.	Right click in empty space
2.	Click Open in Terminal or Open PowerShell window here
You should now be inside:
D:\...\Ayurveda-NER-model-main\SattvaX

3. Install Python Dependencies
Install all required packages using:
pip install -r requirements.txt
This installs:
1.	Flask
2.	spaCy
3.	waitress
4.	requests
5.	other required dependencies


4. Run the Application
After installation completes, run:
python app.py

5. Open the Application in Browser
After running the command, terminal will show something like:
Running on http://127.0.0.1:7860
Open this URL in browser:
http://127.0.0.1:7860
















Installation and execution steps in Terminal:

Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

Loading personal and system profiles took 11634ms.
(base) PS D:\Intern\Rutuparn\Development\SattvaX\Ayurveda-NER-model-main\SattvaX> python app.py
Traceback (most recent call last):
  File "D:\Intern\Rutuparn\Development\SattvaX\Ayurveda-NER-model-main\SattvaX\app.py", line 1, in <module>
    from flask import Flask, render_template, request, jsonify
ModuleNotFoundError: No module named 'flask'
(base) PS D:\Intern\Rutuparn\Development\SattvaX\Ayurveda-NER-model-main\SattvaX> pip install flask
Collecting flask
  Downloading flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
Collecting blinker>=1.9.0 (from flask)
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Requirement already satisfied: click>=8.1.3 in c:\users\pritam\miniconda3\lib\site-packages (from flask) (8.1.8)
Collecting itsdangerous>=2.2.0 (from flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from flask)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from flask)
  Using cached markupsafe-3.0.3-cp313-cp313-win_amd64.whl.metadata (2.8 kB)
Collecting werkzeug>=3.1.0 (from flask)
  Downloading werkzeug-3.1.8-py3-none-any.whl.metadata (4.0 kB)
Requirement already satisfied: colorama in c:\users\pritam\miniconda3\lib\site-packages (from click>=8.1.3->flask) (0.4.6)
Downloading flask-3.1.3-py3-none-any.whl (103 kB)
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached markupsafe-3.0.3-cp313-cp313-win_amd64.whl (15 kB)
Downloading werkzeug-3.1.8-py3-none-any.whl (226 kB)
Installing collected packages: markupsafe, itsdangerous, blinker, werkzeug, jinja2, flask
Successfully installed blinker-1.9.0 flask-3.1.3 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.3 werkzeug-3.1.8
(base) PS D:\Intern\Rutuparn\Development\SattvaX\Ayurveda-NER-model-main\SattvaX> requirements.txt
requirements.txt : The term 'requirements.txt' is not recognized as the name of a cmdlet, function, script file, or
operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try
again.
At line:1 char:1
+ requirements.txt
+ ~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (requirements.txt:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Suggestion [3,General]: The command requirements.txt was not found, but does exist in the current location. Windows PowerShell does not load commands from the current location by default. If you trust this command, instead type: ".\requirements.txt". See "get-help about_Command_Precedence" for more details.
(base) PS D:\Intern\Rutuparn\Development\SattvaX\Ayurveda-NER-model-main\SattvaX> pip install -r requirements.txt
Collecting Flask==3.0.3 (from -r requirements.txt (line 1))
  Downloading flask-3.0.3-py3-none-any.whl.metadata (3.2 kB)
Collecting waitress==3.0.0 (from -r requirements.txt (line 2))
  Downloading waitress-3.0.0-py3-none-any.whl.metadata (4.2 kB)
Collecting spacy>=3.0.0 (from -r requirements.txt (line 3))
  Downloading spacy-3.8.14-cp313-cp313-win_amd64.whl.metadata (28 kB)
Requirement already satisfied: requests>=2.28.0 in c:\users\pritam\miniconda3\lib\site-packages (from -r requirements.txt (line 4)) (2.32.5)
Requirement already satisfied: Werkzeug>=3.0.0 in c:\users\pritam\miniconda3\lib\site-packages (from Flask==3.0.3->-r requirements.txt (line 1)) (3.1.8)
Requirement already satisfied: Jinja2>=3.1.2 in c:\users\pritam\miniconda3\lib\site-packages (from Flask==3.0.3->-r requirements.txt (line 1)) (3.1.6)
Requirement already satisfied: itsdangerous>=2.1.2 in c:\users\pritam\miniconda3\lib\site-packages (from Flask==3.0.3->-r requirements.txt (line 1)) (2.2.0)
Requirement already satisfied: click>=8.1.3 in c:\users\pritam\miniconda3\lib\site-packages (from Flask==3.0.3->-r requirements.txt (line 1)) (8.1.8)
Requirement already satisfied: blinker>=1.6.2 in c:\users\pritam\miniconda3\lib\site-packages (from Flask==3.0.3->-r requirements.txt (line 1)) (1.9.0)
Collecting spacy-legacy<3.1.0,>=3.0.11 (from spacy>=3.0.0->-r requirements.txt (line 3))
  Using cached spacy_legacy-3.0.12-py2.py3-none-any.whl.metadata (2.8 kB)
Collecting spacy-loggers<2.0.0,>=1.0.0 (from spacy>=3.0.0->-r requirements.txt (line 3))
  Using cached spacy_loggers-1.0.5-py3-none-any.whl.metadata (23 kB)
Collecting murmurhash<1.1.0,>=0.28.0 (from spacy>=3.0.0->-r requirements.txt (line 3))
  Using cached murmurhash-1.0.15-cp313-cp313-win_amd64.whl.metadata (2.3 kB)
Collecting cymem<2.1.0,>=2.0.2 (from spacy>=3.0.0->-r requirements.txt (line 3))
  Using cached cymem-2.0.13-cp313-cp313-win_amd64.whl.metadata (9.9 kB)
Collecting preshed<3.1.0,>=3.0.2 (from spacy>=3.0.0->-r requirements.txt (line 3))
  Downloading preshed-3.0.13-cp313-cp313-win_amd64.whl.metadata (5.4 kB)
Collecting thinc<8.4.0,>=8.3.12 (from spacy>=3.0.0->-r requirements.txt (line 3))
  Downloading thinc-8.3.13-cp313-cp313-win_amd64.whl.metadata (15 kB)
Collecting wasabi<1.2.0,>=0.9.1 (from spacy>=3.0.0->-r requirements.txt (line 3))
  Using cached wasabi-1.1.3-py3-none-any.whl.metadata (28 kB)
Collecting srsly<3.0.0,>=2.5.3 (from spacy>=3.0.0->-r requirements.txt (line 3))
  Downloading srsly-2.5.3-cp313-cp313-win_amd64.whl.metadata (20 kB)
Collecting catalogue<2.1.0,>=2.0.6 (from spacy>=3.0.0->-r requirements.txt (line 3))
  Using cached catalogue-2.0.10-py3-none-any.whl.metadata (14 kB)
Collecting weasel<2.0.0,>=1.0.0 (from spacy>=3.0.0->-r requirements.txt (line 3))
  Downloading weasel-1.0.0-py3-none-any.whl.metadata (4.6 kB)
Collecting confection<2.0.0,>=1.3.2 (from spacy>=3.0.0->-r requirements.txt (line 3))
  Downloading confection-1.3.3-py3-none-any.whl.metadata (19 kB)
Requirement already satisfied: typer<1.0.0,>=0.3.0 in c:\users\pritam\miniconda3\lib\site-packages (from spacy>=3.0.0->-r requirements.txt (line 3)) (0.17.4)
Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in c:\users\pritam\miniconda3\lib\site-packages (from spacy>=3.0.0->-r requirements.txt (line 3)) (4.67.1)
Collecting numpy>=1.19.0 (from spacy>=3.0.0->-r requirements.txt (line 3))
  Downloading numpy-2.4.4-cp313-cp313-win_amd64.whl.metadata (6.6 kB)
Requirement already satisfied: pydantic<3.0.0,>=2.0.0 in c:\users\pritam\miniconda3\lib\site-packages (from spacy>=3.0.0->-r requirements.txt (line 3)) (2.12.3)
Requirement already satisfied: setuptools in c:\users\pritam\miniconda3\lib\site-packages (from spacy>=3.0.0->-r requirements.txt (line 3)) (80.9.0)
Requirement already satisfied: packaging>=20.0 in c:\users\pritam\miniconda3\lib\site-packages (from spacy>=3.0.0->-r requirements.txt (line 3)) (25.0)
Requirement already satisfied: charset_normalizer<4,>=2 in c:\users\pritam\miniconda3\lib\site-packages (from requests>=2.28.0->-r requirements.txt (line 4)) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in c:\users\pritam\miniconda3\lib\site-packages (from requests>=2.28.0->-r requirements.txt (line 4)) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\pritam\miniconda3\lib\site-packages (from requests>=2.28.0->-r requirements.txt (line 4)) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\pritam\miniconda3\lib\site-packages (from requests>=2.28.0->-r requirements.txt (line 4)) (2025.10.5)
Requirement already satisfied: annotated-types>=0.6.0 in c:\users\pritam\miniconda3\lib\site-packages (from pydantic<3.0.0,>=2.0.0->spacy>=3.0.0->-r requirements.txt (line 3)) (0.6.0)
Requirement already satisfied: pydantic-core==2.41.4 in c:\users\pritam\miniconda3\lib\site-packages (from pydantic<3.0.0,>=2.0.0->spacy>=3.0.0->-r requirements.txt (line 3)) (2.41.4)
Requirement already satisfied: typing-extensions>=4.14.1 in c:\users\pritam\miniconda3\lib\site-packages (from pydantic<3.0.0,>=2.0.0->spacy>=3.0.0->-r requirements.txt (line 3)) (4.15.0)
Requirement already satisfied: typing-inspection>=0.4.2 in c:\users\pritam\miniconda3\lib\site-packages (from pydantic<3.0.0,>=2.0.0->spacy>=3.0.0->-r requirements.txt (line 3)) (0.4.2)
Collecting blis<1.4.0,>=1.3.0 (from thinc<8.4.0,>=8.3.12->spacy>=3.0.0->-r requirements.txt (line 3))
  Using cached blis-1.3.3-cp313-cp313-win_amd64.whl.metadata (7.7 kB)
Requirement already satisfied: colorama in c:\users\pritam\miniconda3\lib\site-packages (from tqdm<5.0.0,>=4.38.0->spacy>=3.0.0->-r requirements.txt (line 3)) (0.4.6)
Requirement already satisfied: shellingham>=1.3.0 in c:\users\pritam\miniconda3\lib\site-packages (from typer<1.0.0,>=0.3.0->spacy>=3.0.0->-r requirements.txt (line 3)) (1.5.4)
Requirement already satisfied: rich>=10.11.0 in c:\users\pritam\miniconda3\lib\site-packages (from typer<1.0.0,>=0.3.0->spacy>=3.0.0->-r requirements.txt (line 3)) (14.2.0)
Collecting cloudpathlib>=0.7.0 (from weasel<2.0.0,>=1.0.0->spacy>=3.0.0->-r requirements.txt (line 3))
  Downloading cloudpathlib-0.24.0-py3-none-any.whl.metadata (16 kB)
Collecting smart-open>=5.2.1 (from weasel<2.0.0,>=1.0.0->spacy>=3.0.0->-r requirements.txt (line 3))
  Downloading smart_open-7.6.1-py3-none-any.whl.metadata (25 kB)
Collecting httpx>=0.24.0 (from weasel<2.0.0,>=1.0.0->spacy>=3.0.0->-r requirements.txt (line 3))
  Using cached httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting anyio (from httpx>=0.24.0->weasel<2.0.0,>=1.0.0->spacy>=3.0.0->-r requirements.txt (line 3))
  Downloading anyio-4.13.0-py3-none-any.whl.metadata (4.5 kB)
Collecting httpcore==1.* (from httpx>=0.24.0->weasel<2.0.0,>=1.0.0->spacy>=3.0.0->-r requirements.txt (line 3))
  Using cached httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx>=0.24.0->weasel<2.0.0,>=1.0.0->spacy>=3.0.0->-r requirements.txt (line 3))
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\pritam\miniconda3\lib\site-packages (from Jinja2>=3.1.2->Flask==3.0.3->-r requirements.txt (line 1)) (3.0.3)
Requirement already satisfied: markdown-it-py>=2.2.0 in c:\users\pritam\miniconda3\lib\site-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy>=3.0.0->-r requirements.txt (line 3)) (4.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\users\pritam\miniconda3\lib\site-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy>=3.0.0->-r requirements.txt (line 3)) (2.19.2)
Requirement already satisfied: mdurl~=0.1 in c:\users\pritam\miniconda3\lib\site-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy>=3.0.0->-r requirements.txt (line 3)) (0.1.2)
Collecting wrapt (from smart-open>=5.2.1->weasel<2.0.0,>=1.0.0->spacy>=3.0.0->-r requirements.txt (line 3))
  Downloading wrapt-2.1.2-cp313-cp313-win_amd64.whl.metadata (7.6 kB)
Downloading flask-3.0.3-py3-none-any.whl (101 kB)
Downloading waitress-3.0.0-py3-none-any.whl (56 kB)
Downloading spacy-3.8.14-cp313-cp313-win_amd64.whl (14.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.2/14.2 MB 236.9 kB/s  0:00:56
Using cached catalogue-2.0.10-py3-none-any.whl (17 kB)
Downloading confection-1.3.3-py3-none-any.whl (35 kB)
Using cached cymem-2.0.13-cp313-cp313-win_amd64.whl (40 kB)
Using cached murmurhash-1.0.15-cp313-cp313-win_amd64.whl (25 kB)
Downloading preshed-3.0.13-cp313-cp313-win_amd64.whl (122 kB)
Using cached spacy_legacy-3.0.12-py2.py3-none-any.whl (29 kB)
Using cached spacy_loggers-1.0.5-py3-none-any.whl (22 kB)
Downloading srsly-2.5.3-cp313-cp313-win_amd64.whl (650 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 650.8/650.8 kB 370.4 kB/s  0:00:01
Downloading thinc-8.3.13-cp313-cp313-win_amd64.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 386.7 kB/s  0:00:04
Using cached blis-1.3.3-cp313-cp313-win_amd64.whl (6.2 MB)
Downloading numpy-2.4.4-cp313-cp313-win_amd64.whl (12.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 405.3 kB/s  0:00:30
Using cached wasabi-1.1.3-py3-none-any.whl (27 kB)
Downloading weasel-1.0.0-py3-none-any.whl (50 kB)
Downloading cloudpathlib-0.24.0-py3-none-any.whl (63 kB)
Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Downloading smart_open-7.6.1-py3-none-any.whl (64 kB)
Downloading anyio-4.13.0-py3-none-any.whl (114 kB)
Downloading wrapt-2.1.2-cp313-cp313-win_amd64.whl (60 kB)
Installing collected packages: wrapt, wasabi, waitress, spacy-loggers, spacy-legacy, numpy, murmurhash, h11, cymem, confection, cloudpathlib, catalogue, anyio, srsly, smart-open, preshed, httpcore, Flask, blis, thinc, httpx, weasel, spacy
  Attempting uninstall: Flask
    Found existing installation: Flask 3.1.3
    Uninstalling Flask-3.1.3:
      Successfully uninstalled Flask-3.1.3
Successfully installed Flask-3.0.3 anyio-4.13.0 blis-1.3.3 catalogue-2.0.10 cloudpathlib-0.24.0 confection-1.3.3 cymem-2.0.13 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 murmurhash-1.0.15 numpy-2.4.4 preshed-3.0.13 smart-open-7.6.1 spacy-3.8.14 spacy-legacy-3.0.12 spacy-loggers-1.0.5 srsly-2.5.3 thinc-8.3.13 waitress-3.0.0 wasabi-1.1.3 weasel-1.0.0 wrapt-2.1.2
(base) PS D:\Intern\Rutuparn\Development\SattvaX\Ayurveda-NER-model-main\SattvaX> pip list
Package                  Version
------------------------ ---------
anaconda-anon-usage      0.7.4
anaconda-auth            0.10.0
anaconda-cli-base        0.6.0
annotated-types          0.6.0
anyio                    4.13.0
archspec                 0.2.5
blinker                  1.9.0
blis                     1.3.3
boltons                  25.0.0
brotlicffi               1.0.9.2
catalogue                2.0.10
certifi                  2025.10.5
cffi                     2.0.0
charset-normalizer       3.4.4
click                    8.1.8
cloudpathlib             0.24.0
colorama                 0.4.6
conda                    25.9.1
conda-anaconda-telemetry 0.3.0
conda-anaconda-tos       0.2.2
conda-content-trust      0.2.0
conda-libmamba-solver    25.4.0
conda-package-handling   2.4.0
conda_package_streaming  0.12.0
confection               1.3.3
cryptography             46.0.3
cymem                    2.0.13
distro                   1.9.0
Flask                    3.0.3
frozendict               2.4.6
h11                      0.16.0
httpcore                 1.0.9
httpx                    0.28.1
idna                     3.11
itsdangerous             2.2.0
jaraco.classes           3.4.0
jaraco.context           0.0.0
jaraco.functools         4.1.0
Jinja2                   3.1.6
jsonpatch                1.33
jsonpointer              3.0.0
keyring                  25.6.0
libmambapy               2.3.2
markdown-it-py           4.0.0
MarkupSafe               3.0.3
mdurl                    0.1.2
menuinst                 2.4.1
more-itertools           10.8.0
murmurhash               1.0.15
numpy                    2.4.4
packaging                25.0
pip                      25.2
pkce                     1.0.3
platformdirs             4.5.0
pluggy                   1.5.0
preshed                  3.0.13
pycosat                  0.6.6
pycparser                2.23
pydantic                 2.12.3
pydantic_core            2.41.4
pydantic-settings        2.10.1
Pygments                 2.19.2
PyJWT                    2.10.1
PySocks                  1.7.1
python-dotenv            1.1.0
pywin32-ctypes           0.2.2
readchar                 4.2.1
requests                 2.32.5
rich                     14.2.0
ruamel.yaml              0.18.16
ruamel.yaml.clib         0.2.14
semver                   3.0.4
setuptools               80.9.0
shellingham              1.5.4
smart_open               7.6.1
spacy                    3.8.14
spacy-legacy             3.0.12
spacy-loggers            1.0.5
srsly                    2.5.3
thinc                    8.3.13
tomli                    2.2.1
tqdm                     4.67.1
truststore               0.10.1
typer                    0.17.4
typing_extensions        4.15.0
typing-inspection        0.4.2
urllib3                  2.5.0
waitress                 3.0.0
wasabi                   1.1.3
weasel                   1.0.0
Werkzeug                 3.1.8
wheel                    0.45.1
win_inet_pton            1.1.0
wrapt                    2.1.2
zstandard                0.24.0
(base) PS D:\Intern\Rutuparn\Development\SattvaX\Ayurveda-NER-model-main\SattvaX> python app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:7860
 * Running on http://10.208.26.232:7860
Press CTRL+C to quit
127.0.0.1 - - [15/May/2026 11:14:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [15/May/2026 11:14:22] "GET /static/css/style.css?v=2 HTTP/1.1" 200 -
127.0.0.1 - - [15/May/2026 11:14:22] "GET /static/css/style_extras.css?v=3 HTTP/1.1" 200 -
127.0.0.1 - - [15/May/2026 11:14:22] "GET /static/js/main.js?v=11 HTTP/1.1" 200 -
127.0.0.1 - - [15/May/2026 11:14:22] "GET /login HTTP/1.1" 200 -
127.0.0.1 - - [15/May/2026 11:14:23] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [15/May/2026 11:14:27] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [15/May/2026 11:14:28] "GET /static/css/style.css?v=2 HTTP/1.1" 304 -
127.0.0.1 - - [15/May/2026 11:14:28] "GET /static/css/style_extras.css?v=3 HTTP/1.1" 304 -
127.0.0.1 - - [15/May/2026 11:14:28] "GET /static/js/main.js?v=11 HTTP/1.1" 304 -
127.0.0.1 - - [15/May/2026 11:14:33] "POST /analyze HTTP/1.1" 200 -
127.0.0.1 - - [15/May/2026 11:30:41] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [15/May/2026 11:30:41] "GET /static/css/style.css?v=2 HTTP/1.1" 304 -
127.0.0.1 - - [15/May/2026 11:30:41] "GET /static/css/style_extras.css?v=3 HTTP/1.1" 304 -
127.0.0.1 - - [15/May/2026 11:30:41] "GET /static/js/main.js?v=11 HTTP/1.1" 304 -
127.0.0.1 - - [15/May/2026 11:30:45] "POST /analyze HTTP/1.1" 200 -
