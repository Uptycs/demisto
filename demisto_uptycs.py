#!/usr/bin/python

###############################################################################
# import required libraries package
###############################################################################

import os
import sys
import getopt
import json
import jwt
import datetime
import requests
import argparse
import urllib3
from pygments import highlight, lexers, formatters

###############################################################################
# supress traceback call. Use it only for troubleshoot/debug
###############################################################################
sys.tracebacklimit = 0

###############################################################################
# packages to handle IOerror
###############################################################################

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

###############################################################################
# function to generate header
###############################################################################

def generateHeaders(data, key, secret):
    header={}
    utcnow=datetime.datetime.utcnow()
    date=utcnow.strftime("%a, %d %b %Y %H:%M:%S GMT")
    authVar = jwt.encode({'iss': key}, secret, algorithm='HS256').decode('utf-8')
    authorization="Bearer %s" % (authVar)
    header['date']=date
    header['Authorization']=authorization
    return header

###############################################################################
# function for restAPI call
###############################################################################
def restcall(apiconfig, method, api, post_data_file):
    data = apiconfig #json.load(open(apiconfig))

    # JWT encoded header
    header=generateHeaders('' , data['key'] , data['secret'])

    # URL form using API key file
    url=("https://%s.uptycs.io/public/api/customers/%s%s" %
            (data['domain'],data['customerId'],api))

    # GET call of restAPI
    if method == 'GET':
        response = requests.get(url, headers=header, verify=False )

    # POST call for restAPI
    if method == 'POST':
        post_data=post_data_file #json.load(open(post_data_file))
        # This is for debuging printing the post data
        response = requests.post(url, headers=header,
                json=post_data, verify=False )

    if method == 'DELETE':
        # This is for debuging printing the post data
        if post_data_file:
            post_data=post_data_file #json.load(open(post_data_file))
            response = requests.delete(url, headers=header,
                    json=post_data, verify=False )
        else:
            response = requests.delete(url, headers=header, verify=False )

    if method == 'PUT':
        post_data=post_data_file #json.load(open(post_data_file))
        # This is for debuging printing the post data
        response = requests.put(url, headers=header,
                json=post_data, verify=False )

    if (response.status_code != requests.codes.ok):
        sys.exit(1)

    return response.content

###############################################################################
# main function
###############################################################################
if demisto.command() == 'uptycs-example-command':
    demisto.results({'ContentsFormat': formats['json'],
                     'Type': entryTypes['note'],
                     'Contents':{'RawKey': {'RawOtherKey': 'RawValue'}},
                     'HumanReadable': '# My Markdown',
                     'EntryContext':{'SomeKey': {'SomeOtherKey': 'SomeValue'}}})
if demisto.command() == 'uptycs-test-command':
# We want to supress the warnings message
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    apifile = {
        'key':demisto.params()['key'],
        'secret':demisto.params()['secret'],
        'domain':demisto.params()['domain'],
        'customerId':demisto.params()['customerId']
    }
    method = demisto.args()['method']
    api_call = demisto.args()['api_call']
    post_data = {
        'query':demisto.args()['query'],
        'queryType':demisto.args()['queryType']
    }

    # RestCall
    query_results = restcall(apifile, method, api_call, post_data)

    demisto.results({'ContentsFormat': formats['json'],
                     'Type': entryTypes['note'],
                     'Contents':{'RawKey': {'RawOtherKey': 'RawValue'}},
                     'HumanReadable': '# Uptycs Test Connect',
                     'EntryContext': {'TestUptycsKey':json.loads(query_results)}})


    #sys.exit(0)

if demisto.command() == 'get-process-hashes':
# We want to supress the warnings message
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    apifile = {
        'key':demisto.params()['key'],
        'secret':demisto.params()['secret'],
        'domain':demisto.params()['domain'],
        'customerId':demisto.params()['customerId']
    }
    method = demisto.args()['method']
    api_call = demisto.args()['api_call']
    post_data = {
        'query':demisto.args()['query'],
        'queryType':demisto.args()['queryType']
    }

    # RestCall
    query_results = restcall(apifile, method, api_call, post_data)

    demisto.results({'ContentsFormat': formats['json'],
                     'Type': entryTypes['note'],
                     'Contents':{'RawKey': {'RawOtherKey': 'RawValue'}},
                     'HumanReadable': '# Uptycs Test Connect',
                     'EntryContext': {'TestUptycsKey':json.loads(query_results)}})

    #sys.exit(0)
# The command demisto.command() holds the command sent from the user.
if demisto.command() == 'test-module':
    # This is the call made when pressing the integration test button.
    demisto.results('ok')
    sys.exit(0)
if demisto.command() == 'fetch-incidents':
    # You can store the last run time...
    demisto.setLastRun({'time': 'now'})
    # And retrieve it for use later:
    lastRun = demisto.getLastRun()
    # lastRun is a dictionary, with value "now" for key "time".
    # JSON of the incident type created by this integration
    demisto.incidents([{"Name":"Incident #1"},{"Name":"Incident #2"}])
    sys.exit(0)
# You can use demisto.args()[argName] to get a specific arg. args are strings.
# You can use demisto.params()[paramName] to get a specific params.
# Params are of the type given in the integration page creation.
