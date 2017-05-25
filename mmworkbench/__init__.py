# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .app import Application
from ._util import blueprint, configure_logs
from .components import Conversation, NaturalLanguageProcessor, QuestionAnswerer
from ._version import current

__author__ = 'MindMeld, Inc.'
__email__ = 'contact@mindmeld.com'
__version__ = current

__all__ = ['blueprint', 'configure_logs', 'Application', 'Conversation',
           'NaturalLanguageProcessor', 'QuestionAnswerer']