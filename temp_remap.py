#coding=utf-8

def remap_temp(comm_instance, parsed_temperatures, *args, **kwargs):


__plugin_name__ = "Temperature remap"
__plugin_hooks__ = {
   "octoprint.comm.protocol.temperatures.received": remap_temp
}
