#!/usr/bin/python

import stat, sys, os, string, commands

try:

#    user = os.getenv("SUDO_USER")
#    if user is None:
#      print "This program need 'sudo'"
#      sys.exit(1)

    html_dir = raw_input("Enter the top-level directory for installation of multiple sites (defaults to /var/www):\n")

    if not html_dir:
 	html_dir = '/var/www'

    if os.path.isdir(html_dir):
      commandString = "ls " + html_dir 
      commandOutput = commands.getoutput(commandString)
      findResults = string.split(commandOutput, "\n")

      print commandString
      print "======= has these sub-directories ======"
      for line in findResults:
        print line

      print "========================================"
    else:
      print "This home directory doesn't exist on the system...Exiting now."
      sys.exit(1) 

    domains_input = []
    entry = raw_input("Enter the domains, one per line. Enter a blank line to quit: \n")

    while entry:
      domains_input.append(entry)
      entry = raw_input("")

    print "Setting up the domains: "  
    for domain in domains_input:
      print domain

except:
    print "There was a problem - check the message above"
