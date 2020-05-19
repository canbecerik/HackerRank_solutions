# Adapted from https://blog.magrathealabs.com/filesystem-events-monitoring-with-python-9f5329b651c3

import os, time
from watchdog.events import RegexMatchingEventHandler

