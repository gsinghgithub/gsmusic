#!/usr/bin/env python
from GsMidiFile import MIDIFile
from GsMidiFile import TICKSPERBEAT_CONFIG
import re
import struct
import os
import logging
import logging.handlers
import time
from time import gmtime, strftime
print strftime("%Y-%m-%d %H:%M:%S", time.localtime())
logger = logging.getLogger(__name__)
LOGFILE = 'log_midi.txt'
logger.setLevel(logging.DEBUG)
t = time.localtime()
