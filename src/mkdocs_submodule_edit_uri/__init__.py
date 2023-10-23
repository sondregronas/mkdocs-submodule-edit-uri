from importlib.metadata import version, PackageNotFoundError

from mkdocs_submodule_edit_uri.plugin import SubmoduleEditUriPlugin

try:
    __version__ = version('mkdocs-submodule-edit-uri')
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    pass
