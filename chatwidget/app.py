# coding=utf-8

import pymongo
import pkg_resources

from starflyer import Application, URL, AttributeMapper

import widget

### 
### APP
###

class ChatWidgetApp(Application):
    """Chat Widget"""

    defaults = {
        'log_name'              : "chat",
        'virtual_path'          : "",
        'server_name'           : "dev.localhost:9004",
        'title'                 : "Live Chat",
        'description'           : "",
        'debug'                 : False,
        'mongodb_name'          : "ppchat",
        'mongodb_port'          : 27017,
        'mongodb_host'          : "localhost",
        'secret_key'            : "cd9scd8uz9csd87cs9s8cd7s9d87dsj&&&cvgvdsh((ichjbcsjdbhdjhbcjhbds",
        'session_cookie_domain' : "dev.localhost",
        'smtp_host'             : 'localhost',
        'smtp_port'             : 25,
    }

    modules = [
    ]

    routes = [
        URL('/', 'root', widget.Widget),
    ]

    def finalize_setup(self):
        """do our own configuration stuff"""
        self.config.dbs = AttributeMapper()
        mydb = self.config.dbs.db = pymongo.Connection(
            self.config.mongodb_host,
            self.config.mongodb_port
        )[self.config.mongodb_name]


def app(config, **local_config):
    """return the config""" 
    return ChatWidgetApp(__name__, local_config)

