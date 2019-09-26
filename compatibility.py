#coding=utf-8

import logging
from octoprint.util.commandline import CommandLineCaller

firmware = null

def on_after_startup()
    caller.call("M115");
    logging.getLogger("octoprint.plugin." + __name__).info("sending m115")

def detect_fw(comm, line, *args, **kwargs):
    if line.contains("ZWLF"):
        logging.getLogger("octoprint.plugin." + __name__).info("Firmware detected: Chitu.\nEnabling bugfixes.." + comm)
    return

__plugin_name__ = "fwfix"
__plugin_hooks__ = {
    "octoprint.comm.protocol.gcode.received": detect_fw
}
