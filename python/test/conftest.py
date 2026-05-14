import glob
import os
import shutil
import sys
from collections.abc import Iterator

sys.path.append('./src')


import pytest


@pytest.fixture(autouse=True)
def _cleanup_pycaches() -> Iterator[None]:
    before = set(glob.glob(os.path.join('.', '**', '__pycache__'), recursive=True))
    yield
    for pycache in before:
        if os.path.exists(pycache):
            shutil.rmtree(pycache)


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
