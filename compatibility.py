#coding=utf-8

from octoprint.util.commandline import CommandLineCaller
import octoprint.plugin
import logging

caller = CommandLineCaller()

class Plugin(octoprint.plugin.EventHandlerPlugin):
  on_event(event, payload):
    if event == "Connected":
      caller.call(["M115"])
  
  gcode_rec(comm_instance, line, *args, **kwargs):
    if "ZWLF make it" is in line:
      fwtype = 1 #ChiTu
      return line
    if 
      
      


__plugin_name__ = "fwfix"
__plugin_author__ = "nocem"
__plugin_version__ = "0.0.1"
__plugin_hooks__ = {
  "octoprint.comm.protocol.gcode.received": gcode_rec
}
__plugin_implementation__ = Plugin()
