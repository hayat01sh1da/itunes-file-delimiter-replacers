import pytest
import re
import os
import shutil
import sys
from collections.abc import Iterator

sys.path.append('./src')


@pytest.fixture(autouse=True)
def __cleanup_caches__() -> Iterator[None]:
    yield
    cache_dir = re.compile(r'^(?:__pycache__|\.pytest_cache|\.mypy_cache)$')
    for root, dirs, _ in os.walk('.'):
        for name in list(dirs):
            if cache_dir.match(name):
                shutil.rmtree(os.path.join(root, name), ignore_errors=True)
                dirs.remove(name)


@pytest.fixture
def base_dir() -> Iterator[str]:
    directory = os.path.join('.', 'test', 'Artist')
    paths = (
        os.path.join(directory, 'Album1', '1-01 Title.m4a'),
        os.path.join(directory, 'Album1', '2-01 Title.m4a'),
        os.path.join(directory, 'Album2', '01 Title.m4a'),
        os.path.join(directory, 'Album2', '02 Title.m4a'),
        os.path.join(directory, 'Album3', '01 Title.mp3'),
    )
    for path in paths:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write('')
    yield directory
    if os.path.exists(directory):
        shutil.rmtree(directory)
