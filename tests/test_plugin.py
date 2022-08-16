import pytest

from mkdocs_submodule_edit_uri import SubmoduleEditUriPlugin


@pytest.fixture
def plugin():
    plugin = SubmoduleEditUriPlugin()
    plugin.load_config(
        options={"repo_url": 'https://github.com/user/repo',
                 'edit_uri': 'edit/main/docs'
                 }
    )
    plugin.on_config(plugin.config)
    return plugin


def test_plugin(plugin):
    plugin.config['modules'] = [
        {'test': {'old': 'https://github.com/user/repo/docs/submodule', 'new': 'https://github.com/user/repo-submodule'}}
    ]
    plugin.on_config(None)

    test = plugin.on_post_page('https://github.com/user/repo/docs/submodule/edit', None, None)
    assert 'https://github.com/user/repo-submodule/edit' in str(test)

    test = plugin.on_post_page('https://github.com/user/repo/docs/normal/edit', None, None)
    assert 'https://github.com/user/repo-submodule/edit' not in str(test)
    assert 'https://github.com/user/repo/docs/normal/edit' in str(test)

    # Multiple values
    plugin.config['modules'] = [
        {'test': {'old': 'https://github.com/user/repo/docs/submodule', 'new': 'https://github.com/user/repo-submodule'},
         'test2': {'old': 'https://github.com/user/repo/docs/sub2', 'new': 'https://github.com/user/repo-submodule2'}}
    ]
    plugin.on_config(None)

    test = plugin.on_post_page('https://github.com/user/repo/docs/submodule/edit', None, None)
    assert 'https://github.com/user/repo-submodule/edit' in str(test)
    test = plugin.on_post_page('https://github.com/user/repo/docs/sub2/edit', None, None)
    assert 'https://github.com/user/repo-submodule2/edit' in str(test)
    test = plugin.on_post_page('https://github.com/user/repo/docs/normal/edit', None, None)
    assert 'https://github.com/user/repo/docs/normal/edit' in str(test)
