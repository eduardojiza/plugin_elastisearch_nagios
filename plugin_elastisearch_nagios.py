#!/usr/bin/python
import urllib, json
import os, sys

argumentos = sys.argv
cadHost = "localhost"
cadPort = "9200"

if "-H" in argumentos:
	hostIndex = argumentos.index("-H")
	cadHost = argumentos[hostIndex+1]

if "-P" in argumentos:
	portIndex = argumentos.index("-P")
	cadPort = argumentos[portIndex+1]

ip = cadHost
port = cadPort
url = "http://%s:%s/_cluster/health?pretty" % (ip, port,)
try:
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	name =  data["cluster_name"]
	status = data["status"]
	#status = "green"
	activeShards = data["active_shards"]
except Exception:
	status = "UNKNOW"


if status == "green":
	print "OK - Name: %s is %s with active shards: %s" % (name, status, activeShards)
	sys.exit(0)
elif status == "yellow":
	print "WARNING - Name: %s is %s with active shards: %s" % (name, status, activeShards)
	sys.exit(1)
elif status == "red":
	print "CRITICAL - Name: %s is %s with active shards: %s" % (name, status, activeShards)
	sys.exit(2)
else:
	print "UKNOWN - %s:%s " % (ip, port,)
	sys.exit(3)
