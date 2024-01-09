#!/usr/bin/env python3

# Script Name:                  ops401d8-day02
# Author:                       Maatthew Earles
# Date of latest revision:      01/09/2024
# Purpose:                      Uptime Sensor Tool

# import Libraries
import os
import datetime
import time

# Main 
# Transmit a single ICMP (ping) packet to a specific IP.
# Evaluate the response as success/failure. 0 = success
# Credit to ChatGPT for helping with line 19 - to send output to null device
# Source: https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-02/challenges/class_demo.py  and https://github.com/codefellows/seattle-cybersecurity-401d10/tree/main/class-02/challenges

def ping(host):
  # Use the os.system function to execute the ping command and redirect output to /dev/null
    response = os.system("ping -c 1 " + host + " > /dev/null 2>&1")
  # Return True if the response code is 0 (success), otherwise return False
    return response == 0

# prints the status and timestamp for destination IP tested
def print_status(timestamp, host, status):
   # Print the timestamp, host IP, and the status (Success or Failure)
    print(f"[{timestamp}] Host: {host} - Status: {'Success' if status else 'Failure'}")
# Creates infinite loop with 2 second delay
def uptime_sensor(host):
    while True:
      # Get the current timestamp in the specified format
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      # Check the status of the host by calling the ping function
        status = ping(host)
      # Print the status information
        print_status(timestamp, host, status)
      # Sleep for 2 seconds before the next iteration
        time.sleep(2)

#input host IP and run loop
host_to_check = "8.8.8.8"
uptime_sensor(host_to_check)
