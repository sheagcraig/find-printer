#!/usr/bin/python

import sys
import jss
jssPrefs = jss.JSSPrefs()
j = jss.JSS(jssPrefs)

if len(sys.argv) > 1:
    all_policies = j.Policy().retrieve_all()

    #for policy in all_policies:
    #    for printer in policy.findall('printers/printer'):
    #        if printer.findtext('name') == 'LSCopier':
    #            print('Found in %s: %s' % (policy.id, policy.name))
    for search_name in sys.argv[1:]:
        print "Searching for %s" % search_name
        results = [(policy.id, policy.name) for policy in all_policies for printer in policy.findall('printers/printer') if printer.findtext('name') == search_name]
        for result in results:
            print('Found in %s: %s' % result)
