#! /usr/bin/env python

#----------------------------------------------------------------------------------
# Descripcion:
# 
# Modo de ejecucion:
#  
# Fecha Modificacion: 15 NOV 2016
# Autor: JCRAMIREZ
#----------------------------------------------------------------------------------

#***********************************************************
# Library Load
#***********************************************************
import os, sys, time, select, traceback, smtplib, datetime, argparse, re, telnetlib, getpass

#***********************************************************
# Global Variables
#***********************************************************
server="192.168.2.12"
port=5001
telnet_timeout = 1 
 
#***********************************************************
# Funtions
#*********************************************************** 

def main():
	__author__ = 'jcramirez'
	parser = argparse.ArgumentParser(description='Descripcion del APP')
	parser.add_argument('-c','--cmd',help='Command to be summited', required=True)
	args = parser.parse_args()
	   
#*****************************************************
#		MAIN 
#*****************************************************
if __name__ == "__main__":
    main ()
