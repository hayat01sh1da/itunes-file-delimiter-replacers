import os
import sys

from invoke import Context, task

_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_ROOT, 'src'))

from application import Application  # noqa: E402


@task
def run_itunes_file_delimiter_replacer(c: Context) -> None:
    """Run iTunes File Delimiter Replacer"""
    print('Provide the target extension of files whose delimiter you '
          'would like to make changes to(e.g., .m4a)')
    extension = input().strip()

    print('Provide the delimiter you would like to replace the original '
          'one with(Default: `_`)')
    delimiter = input().strip()

    print('Provide d(dry_run: default) to make sure what directories '
          'and files are to be delete first. Then, provide e(execution) '
          'if you would truly like to delete the files. This operation '
          'is cannot be undone, so be alert to your operation!')
    mode = input().strip()

    params: dict[str, str] = {}
    for key, value in {
        'extension': extension, 'delimiter': delimiter, 'mode': mode,
    }.items():
        if value:
            params[key] = value

    Application.run(**params)


@task(default=True)
def test(c: Context) -> None:
    """Run all tests"""
    c.run('pytest .')
