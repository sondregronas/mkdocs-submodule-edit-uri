from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options


class SubmoduleEditUriPlugin(BasePlugin):
    config_scheme = {
        ('modules', config_options.Type(list, default=[]))
    }

    def on_config(self, config):
        self.config['tuples'] = list()
        for x in self.config.get('modules'):
            for y in x.values():
                self.config['tuples'].append(y)

    def on_post_page(self, output, page, config):
        separator = '-'
        for v in self.config['tuples']:
            old = v['old'] + page.url[len(v['old'].split('/')[-1]):-1].replace('%20', ' ')
            new = v['new'] + page.url[len(page.url.split('/')[0]):-1].replace(separator, '%20').replace('%20%20%20', f'%20{separator}%20')

            output = output.replace(f'{old}/index.md', f'{new}/index.md')
            output = output.replace(f'{old}.md', f'{new}.md')

        return output
