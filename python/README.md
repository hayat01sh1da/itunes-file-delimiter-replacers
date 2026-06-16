## 1. Environment

- Python 3.14.6
- pip 26.1.2

## 2. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 3. Execution

```command
$ invoke run_itunes_file_delimiter_replacer
Provide the target extension of files whose delimiter you would like to make changes to(e.g., .m4a)
.m4a
Provide the delimiter you would like to replace the original one with(Default: `_`)
_
Provide d(dry_run: default) to make sure what directories and files are to be delete first. Then, provide e(execution) if you would truly like to delete the files. This operation is cannot be undone, so be alert to your operation!
e
Target extension is `.m4a`
========== [EXECUTION] Total File Count to Clean: 4 ==========
========== [EXECUTION] The delimiters of those files will be replaced with `_` ==========
========== [EXECUTION] Start! ==========
========== [EXECUTION] Replacing the delimiter: `./Artist/Album1/1-01 Title.m4a` => ./Artist/Album1/Disc1/01_Title.m4a` ==========
========== [EXECUTION] Replacing the delimiter: `./Artist/Album1/2-01 Title.m4a` => ./Artist/Album1/Disc2/01_Title.m4a` ==========
========== [EXECUTION] Replacing the delimiter: `./Artist/Album2/01 Title.m4a` => ./Artist/Album2/01_Title.m4a` ==========
========== [EXECUTION] Replacing the delimiter: `./Artist/Album2/02 Title.m4a` => ./Artist/Album2/02_Title.m4a` ==========
========== [EXECUTION] Done! ==========
========== [EXECUTION] Total Target File Count: 4 ==========
```

## 4. Unit Test

```command
$ invoke
============================= test session starts ==============================
platform linux -- Python 3.14.6, pytest-9.0.3, pluggy-1.6.0
rootdir: itunes-file-delimiter-replacers/python
configfile: pyproject.toml
collected 4 items

test/test_application.py ....                                            [100%]

============================== 4 passed in 0.89s ===============================
```

## 5. Static Code Analysis

```command
$ flake8 .
./src/application.py:35:80: E501 line too long (81 > 79 characters)
./src/application.py:48:80: E501 line too long (88 > 79 characters)
./src/application.py:66:80: E501 line too long (101 > 79 characters)
./src/application.py:69:80: E501 line too long (87 > 79 characters)
./src/application.py:69:80: E501 line too long (87 > 79 characters)
./src/application.py:76:80: E501 line too long (98 > 79 characters)
./src/application.py:85:80: E501 line too long (99 > 79 characters)
./src/application.py:90:80: E501 line too long (85 > 79 characters)
./src/application.py:102:80: E501 line too long (82 > 79 characters)
./src/application.py:114:80: E501 line too long (87 > 79 characters)
./test/test_application.py:23:80: E501 line too long (82 > 79 characters)
$ autoflake8 --in-place --remove-duplicate-keys --remove-unused-variables --recursive .
$ autopep8 --in-place --aggressive --aggressive --recursive .
```

## 6. Type Checks

```command
$ mypy .
Success: no issues found in 4 source files
```
