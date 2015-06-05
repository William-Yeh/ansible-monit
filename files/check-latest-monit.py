#!/usr/bin/env python
#
# Check the version of latest binary distribution of monit.
#
# USAGE:
#     progname
#
#
# @see https://mmonit.com/monit/dist/binary/
#

import sys
import re
import urllib2
import ssl


MONIT_DIST_LINK = "http://mmonit.com/monit/dist/binary/"

REGEX_MONIT_LIST = re.compile('\salt="\[DIR\]"></td><td><a href="([^"]+)/"')
monit_versions = []


def enumerate_versions():
    global monit_versions
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'}
    req = urllib2.Request(MONIT_DIST_LINK, None, headers)

    f = None
    try:
        f = urllib2.urlopen(req)
    except IOError:
        # ignore [SSL: CERTIFICATE_VERIFY_FAILED] error;
        # @see http://stackoverflow.com/a/28052583/714426
        context = ssl._create_unverified_context()
        f = urllib2.urlopen(req, context=context)

    content = f.read()
    #print content
    for line in content.splitlines():
        m = REGEX_MONIT_LIST.search(line)
        if m:
            monit_versions.append(m.group(1))


def report_latest_version():
    print '{ "ok": true, "version": "%s" }' % monit_versions[-1]
    sys.exit(0)


def report_none():
    print '{ "ok": false, "version": "0" }'
    sys.exit(0)


try:
    enumerate_versions()
    if len(monit_versions) > 0:
        report_latest_version()
    else:
        report_none()
except IOError:
    report_none()
