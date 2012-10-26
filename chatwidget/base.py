# encoding=utf-8
import starflyer
from starflyer import redirect
import functools
import random

__all__ = ["BaseHandler"]

class BaseHandler(starflyer.Handler):
    """an extended handler """

    def before(self):
        """prepare the handler"""
        super(BaseHandler, self).before()

    @property
    def render_context(self):
        """provide more information to the render method"""
        payload = dict(
            r = str(random.randint(0,100000))
        )

        return payload

