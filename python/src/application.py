import glob
import inspect
import os
import re
import shutil


class Application:
    """Walks the current directory looking for media files with the given
    extension and rewrites their filenames so the space delimiter becomes a
    configurable character (and `N-` disc prefixes become `DiscN/`
    subdirectories)."""

    class InvalidModeError(Exception):
        pass

    @classmethod
    def run(cls, extension: str = '.m4a', delimiter: str = '_',
            mode: str = 'd') -> None:
        instance = cls(extension=extension, delimiter=delimiter, mode=mode)
        instance.validate_mode()
        instance.replace()

    def __init__(self, extension: str = '.m4a', delimiter: str = '_',
                 mode: str = 'd') -> None:
        self._extension = extension
        self._delimiter = delimiter
        self._mode = mode
        self._paths = glob.glob(
            os.path.join('.', '**', f'*{extension}'), recursive=True)

    def validate_mode(self) -> None:
        match self._mode:
            case 'd' | 'e':
                return
            case _:
                raise self.InvalidModeError(
                    f'{self._mode} is invalid mode. '
                    'Provide either `d`(default) or `e`.'
                )

    def replace(self) -> None:
        self._output(f'Target extension is `{self._extension}`')
        if not self._paths:
            self._announce_empty()
            return
        self._announce_start()
        self._apply_renames()
        self._announce_finish()

    # private

    def _announce_empty(self) -> None:
        self._output(
            f'========== [{self._exec_mode()}] '
            f'No {self._extension} Remains ==========')

    def _announce_start(self) -> None:
        self._output(
            f'========== [{self._exec_mode()}] '
            f'Total File Count to Clean: {len(self._paths)} ==========')
        self._output(
            f'========== [{self._exec_mode()}] '
            f'The delimiters of those files will be replaced with '
            f'`{self._delimiter}` =========='
        )
        self._output(f'========== [{self._exec_mode()}] Start! ==========')

    def _announce_finish(self) -> None:
        self._output(f'========== [{self._exec_mode()}] Done! ==========')
        self._output(
            f'========== [{self._exec_mode()}] '
            f'Total Target File Count: {len(self._paths)} ==========')

    def _apply_renames(self) -> None:
        for before, after in self._file_conversion_map().items():
            self._output(
                f'========== [{self._exec_mode()}] '
                f'Replacing the delimiter: `{before}` => `{after}` ==========')
            if self._mode == 'e':
                self._rename(before, after)

    def _rename(self, before: str, after: str) -> None:
        if re.search(r'Disc\d/', after):
            os.makedirs(os.path.dirname(after), exist_ok=True)
        if before != after:
            shutil.move(before, after)

    def _file_conversion_map(self) -> dict[str, str]:
        if not hasattr(self, '_cached_conversion_map'):
            self._cached_conversion_map = {
                path: self._after(path) for path in self._paths
            }
        return self._cached_conversion_map

    def _after(self, path: str) -> str:
        elements = path.split('/')
        elements[-1] = self._rewrite_filename(elements[-1])
        return '/'.join(elements)

    def _rewrite_filename(self, filename: str) -> str:
        if not re.match(r'^\d-', filename):
            return re.sub(
                r'(?P<track_number>\d{2})\s',
                rf'\g<track_number>{self._delimiter}',
                filename,
            )
        return re.sub(
            r'(?P<disc_number>Disc\d)/(?P<track_number>\d{2})\s',
            rf'\g<disc_number>/\g<track_number>{self._delimiter}',
            re.sub(
                r'^(?P<disc_number>\d)-',
                r'Disc\g<disc_number>/',
                filename,
            ),
        )

    def _exec_mode(self) -> str:
        return 'EXECUTION' if self._mode == 'e' else 'DRY RUN'

    def _test_env(self) -> bool:
        stack = inspect.stack()
        if not stack:
            return False
        return 'pytest' in os.path.basename(stack[-1].filename)

    def _output(self, message: str) -> None:
        if not self._test_env():
            print(message)
