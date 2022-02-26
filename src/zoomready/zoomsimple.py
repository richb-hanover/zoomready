# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 09:49:24 2021

@author: tevsl
"""
version="1.1.1"

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import time
import operator
import psutil
from datetime import timedelta
import webbrowser
import sys
import os
#import argparse    
import warnings
warnings.filterwarnings("ignore")
import ping3
ping3.EXCEPTIONS = True
import versionutils
from cloudflarepycli import cloudflareclass

while (1==1):
    ping3("1.1.1.1")
    time.sleep(1)

print("goodbye")