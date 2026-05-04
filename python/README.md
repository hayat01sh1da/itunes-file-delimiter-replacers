## 1. Environment

- Python 3.14.4

## 2. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 3. Execution

```command
$ python main.py
Provide the target extension of files whose delimiter you would like to make changes to: .m4a
Provide the delimiter to replace spaces with (default `_`): _
Provide the mode (`d` for dry-run, `e` for execution). Default is `d`: e
Target extension is `.m4a`
========== [EXECUTION] Total File Count to Clean: 4 ==========
========== [EXECUTION] The delimiters of those files will be replaced with `_` ==========
========== [EXECUTION] Start! ==========
========== [EXECUTION] Replacing the delimiter: `./Artist/Album1/Disc1/01_Title.m4a` => `./Artist/Album1/Disc1/01_Title.m4a` ==========
========== [EXECUTION] Replacing the delimiter: `./Artist/Album1/Disc2/01_Title.m4a` => `./Artist/Album1/Disc2/01_Title.m4a` ==========
========== [EXECUTION] Replacing the delimiter: `./Artist/Album2/01_Title.m4a` => `./Artist/Album2/01_Title.m4a` ==========
========== [EXECUTION] Replacing the delimiter: `./Artist/Album2/02_Title.m4a` => `./Artist/Album2/02_Title.m4a` ==========
========== [EXECUTION] Done! ==========
========== [EXECUTION] Total Target File Count: 4 ==========
```

## 4. Unit Test

```command
$ pytest 
============================= test session starts ==============================
platform linux -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0
rootdir: /mnt/c/Users/binlh/Documents/development/itunes-file-delimiter-replacers/python
configfile: pyproject.toml
collected 4 items

test/test_application.py ....                                            [100%]

============================== 4 passed in 0.67s ===============================
```
