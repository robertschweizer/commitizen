from typing import Optional


class BaseConfig:
    def __init__(self):
        self._settings: dict = {
            "name": "cz_conventional_commits",
            "version": None,
            "files": [],
            "tag_format": None,  # example v$version
            "bump_message": None,  # bumped v$current_version to $new_version
        }
        self._path: Optional[str] = None

    @property
    def settings(self):
        return self._settings

    @property
    def path(self):
        return self._path

    def set_key(self, key, value):
        """Set or update a key in the conf.

        For now only strings are supported.
        We use to update the version number.
        """
        return self

    def update(self, data: dict):
        self._settings.update(data)

    def add_path(self, path: str):
        self._path = path

    def _parse_setting(self, data: str) -> dict:
        raise NotImplementedError()
