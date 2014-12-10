#!/bin/bash
# Tom LeBrun
# Mod Hist:
# Created 121014
# Modified
# 
# The follwoing program shuts down a instance if no one is logged in. 

/bin/netstat -a| grep mikey | grep EST  > /dev/null 2>&1  # Checks for port 2269
if [ $? -gt 0 ]
then
   # No one is logged in, shut'er down
   /sbin/shutdown -h now
fi
