from __future__ import unicode_literals

from mopidy.backends.local import actor

from tests import unittest, path_to_data_dir
from tests.backends.base.library import LibraryControllerTest


class LocalLibraryControllerTest(LibraryControllerTest, unittest.TestCase):
    backend_class = actor.LocalBackend
    config = {
        'local': {
            'media_dir': path_to_data_dir(''),
            'playlists_dir': '',
            'tag_cache_file': path_to_data_dir('library_tag_cache'),
        }
    }
