import glob
import os

import pytest

from application import Application, InvalidModeError


def _list_files(base_dir: str) -> list[str]:
    return sorted(
        glob.glob(
            os.path.join(
                base_dir,
                '**',
                '*.*'),
            recursive=True))


def test_invalid_mode(base_dir: str) -> None:
    with pytest.raises(InvalidModeError) as excinfo:
        Application(mode='a').run()
    assert str(
        excinfo.value) == 'a is invalid mode. Provide either `d`(default) or `e`.'


def test_dry_run_keeps_original_files(base_dir: str) -> None:
    Application().run()
    assert _list_files(base_dir) == [
        './test/Artist/Album1/1-01 Title.m4a',
        './test/Artist/Album1/2-01 Title.m4a',
        './test/Artist/Album2/01 Title.m4a',
        './test/Artist/Album2/02 Title.m4a',
        './test/Artist/Album3/01 Title.mp3',
    ]


def test_execution_mode_restructures_files(base_dir: str) -> None:
    Application(mode='e').run()
    assert _list_files(base_dir) == [
        './test/Artist/Album1/Disc1/01_Title.m4a',
        './test/Artist/Album1/Disc2/01_Title.m4a',
        './test/Artist/Album2/01_Title.m4a',
        './test/Artist/Album2/02_Title.m4a',
        './test/Artist/Album3/01 Title.mp3',
    ]


def test_execution_mode_with_custom_delimiter(base_dir: str) -> None:
    Application(delimiter='-', mode='e').run()
    assert _list_files(base_dir) == [
        './test/Artist/Album1/Disc1/01-Title.m4a',
        './test/Artist/Album1/Disc2/01-Title.m4a',
        './test/Artist/Album2/01-Title.m4a',
        './test/Artist/Album2/02-Title.m4a',
        './test/Artist/Album3/01 Title.mp3',
    ]
