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
            output = output.replace(v['old'], v['new'])
        return output
