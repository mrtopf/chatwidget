#encoding=utf8

from starflyer import Handler, redirect, asjson
from chatwidget.base import BaseHandler
import datetime

class Widget(BaseHandler):
    """show the chat widget"""

    template = "index.html"

    def get(self):
        """render the view"""
        return self.render()

