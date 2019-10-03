#coding=utf-8

from octoprint.util.commandline import CommandLineCaller
import octoprint.plugin
import logging

class Plugin(octoprint.plugin.EventHandlerPlugin):


__plugin_name__ = "fwfix"
__plugin_author__ = "nocem"
__plugin_version__ = "0.0.1"
__plugin_implementation__ = Plugin()
