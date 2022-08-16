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
        for v in self.config['tuples']:
            old = v['old'][:-len(v['old'].split('/')[-1])] + page.url[:-1]
            new = v['new']+page.url[len(page.url.split('/')[0]):].replace('-', '%20')[:-1]
            output = output.replace(old, new)
        return output
