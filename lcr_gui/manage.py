#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    sys.path.append('C:\\Users\\Eusebio Olalde\\Documents\\E4980A RMT-CTRL\\lcr_com')    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lcr_gui.settings")

    from django.core.management import execute_from_command_line
    
    execute_from_command_line(sys.argv)
