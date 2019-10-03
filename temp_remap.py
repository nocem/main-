#coding=utf-8

def remap_temp(comm_instance, parsed_temperatures, *args, **kwargs):
   return 12.3

__plugin_name__ = "Temperature remap"
__plugin_author__ = "nocem"
__plugin_version__ = "1.0"
__plugin_url__ = "https://github.com/nocem/main-/blob/3d-printing/temp_remap.py"
__plugin_hooks__ = {
   "octoprint.comm.protocol.temperatures.received": remap_temp
}
