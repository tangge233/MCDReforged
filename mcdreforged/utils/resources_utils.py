"""
Resource files / Inner modules getters
Don't run it directly
"""
import pkgutil
from typing import Optional

__all__ = [
	'ROOT_PACKAGE',
	'get_data', 'get_yaml'
]

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

from mcdreforged.constants import core_constant

ROOT_PACKAGE = core_constant.PACKAGE_NAME


def __get_path(path: str) -> str:
	if path.startswith('/'):
		path = path[1:]
	return path


def get_data(path: str) -> Optional[bytes]:
	return pkgutil.get_data(ROOT_PACKAGE, __get_path(path))


def get_yaml(path: str) -> CommentedMap:
	bytes_data = get_data(path)
	# Replace CRLF or yaml loader will load extra lines
	string_data = bytes_data.decode('utf8').replace('\r\n', '\n')
	ret = YAML().load(string_data)
	return ret


if __name__ == '__main__':
	raise RuntimeError("Don't run it directly")
