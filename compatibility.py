#coding=utf-8

from octoprint.util.commandline import CommandLineCaller
import octoprint.plugin

caller = CommandLineCaller()
fwtype = 0 #undefined

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
    if fwtype == 1 && gcode == "M110":
      return "M110"
    
    return

__plugin_name__ = "fwfix"
__plugin_author__ = "nocem"
__plugin_version__ = "0.1.0"
__plugin_hooks__ = {
  "octoprint.comm.protocol.gcode.received": gcode_rec,
  "octoprint.comm.protocol.gcode.queing": gcode_que
}
__plugin_implementation__ = Plugin()
