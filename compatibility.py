#coding=utf-8

from octoprint.util.commandline import CommandLineCaller
import octoprint.plugin

caller = CommandLineCaller()
fwtype = 0 #undefined
ignoredErrors_1 = []  #TODO sd print finished error

class Plugin(octoprint.plugin.EventHandlerPlugin):
  def on_event(event, payload):
    if event == "Connected":
      caller.call(["M115"])
  
  def gcode_rec(comm_instance, line, *args, **kwargs):
    if "ZWLF make it" is in line:
      fwtype = 1 #ChiTu
    
    if fwtype == 1 && line.startswith("wait"):
      return "echo:busy processing"
    
    return line
  
  def gcode_que(comm_instance, phase, cmd, cmd_type, gcode, subcode=None, tags=None, *args, **kwargs):
    if fwtype == 1 && gcode.startswith("M110"):
      return "M110"
    
    return
  
  def gcode_err(comm_instance, error_message, *args, **kwargs):
    if fwtype == 1 && error_message.lower().contains(any(ignoredErrors_1)):
      return True
    

__plugin_name__ = "Extended compatibility"
__plugin_description__ = "This plugin adds extended compatibility(e.g. bugfixes) for ChiTu."
__plugin_author__ = "nocem"
__plugin_version__ = "0.0.5"
__plugin_hooks__ = {
  "octoprint.comm.protocol.gcode.received": gcode_rec,
  "octoprint.comm.protocol.gcode.queing": gcode_que,
  "octoprint.comm.protocol.gcode.error": gcode_err
}
__plugin_implementation__ = Plugin()
