#!/usr/bin/env python
# Copyright (c) 2002-2005 ActiveState Corp.
# See LICENSE.txt for license details.
# Author:
#   Trent Mick (TrentM@ActiveState.com)
# Home:
#   http://trentm.com/projects/px/

"""Test p4lib.py's interface to 'p4 client'."""

import os
import sys
import unittest
import pprint

import testsupport
from p4lib import P4, P4LibError


class ClientTestCase(unittest.TestCase):
    #TODO:
    # - test expected error from trying to change a locked client from a
    #   user that is not the owner
    # - have the super user change a locked client with and without force
    def test_get_client(self):
        top = os.getcwd()
        andrew = testsupport.users['andrew']
        p4 = P4()

        try:
            os.chdir(andrew['home'])

            name = p4.clients()[0]['client']
            client = p4.client(name=name)
            self.failUnless(client['client'] == name)
            self.failUnless(client.has_key('access'))
            self.failUnless(client.has_key('description'))
            self.failUnless(client.has_key('lineend'))
            self.failUnless(client.has_key('options'))
            self.failUnless(client.has_key('owner'))
            self.failUnless(client.has_key('root'))
            self.failUnless(client.has_key('update'))
            self.failUnless(client.has_key('view'))
        finally:
            os.chdir(top)

    def test_delete_recreate_client(self):
        top = os.getcwd()
        andrew = testsupport.users['andrew']
        p4 = P4()

        try:
            os.chdir(andrew['home'])

            name = testsupport.users['bertha']['client']
            clientBefore = p4.client(name=name)

            # Delete the client.
            result = p4.client(name=name, delete=1)
            self.failUnless(result['client'] == name)
            self.failUnless(result['action'] == "deleted")

            # Re-create the client.
            result = p4.client(client=clientBefore)
            self.failUnless(result['client'] == name)
            self.failUnless(result['action'] == "saved")

            # Check that the client is now still the same.
            clientAfter = p4.client(name=name)
            self.failUnless(clientBefore['description'] ==\
                            clientAfter['description'])
            self.failUnless(clientBefore['lineend'] ==\
                            clientAfter['lineend'])
            self.failUnless(clientBefore['options'] ==\
                            clientAfter['options'])
            self.failUnless(clientBefore['owner'] ==\
                            clientAfter['owner'])
            self.failUnless(clientBefore['root'] ==\
                            clientAfter['root'])
            self.failUnless(clientBefore['view'] ==\
                            clientAfter['view'])
        finally:
            os.chdir(top)

    def test_update_client(self):
        top = os.getcwd()
        andrew = testsupport.users['andrew']
        p4 = P4()

        try:
            os.chdir(andrew['home'])

            desc = 'test_update_client'
            name = testsupport.users['bertha']['client']
            clientBefore = p4.client(name=name)

            # Update the client.
            result = p4.client(name=name, client={'description':desc})
            self.failUnless(result['client'] == name)
            self.failUnless(result['action'] == "saved")

            # Cleanup.
            result = p4.client(client=clientBefore)
        finally:
            os.chdir(top)

    def test_update_client_no_change(self):
        top = os.getcwd()
        andrew = testsupport.users['andrew']
        p4 = P4()

        try:
            os.chdir(andrew['home'])

            desc = 'test_update_client'
            name = testsupport.users['bertha']['client']
            clientBefore = p4.client(name=name)

            # Update the client.
            result = p4.client(name=name, client={})
            self.failUnless(result['client'] == name)
            self.failUnless(result['action'] == "not changed")

            # Cleanup.
            result = p4.client(client=clientBefore)
        finally:
            os.chdir(top)

    def test_create_client_hit_license_limit(self):
        top = os.getcwd()
        andrew = testsupport.users['andrew']
        p4 = P4()

        try:
            os.chdir(andrew['home'])

            # Working without a license there should only be two clients
            # allowed, both of which are taken up by the test harness.
            client = {
                'client': 'test_create_client_hit_license_limit',
                'description': 'test_create_client_hit_license_limit',
            }
            self.failUnlessRaises(P4LibError, p4.client, client=client)
        finally:
            os.chdir(top)

    def test_get_client_use_label_name(self):
        top = os.getcwd()
        andrew = testsupport.users['andrew']
        p4 = P4()

        try:
            os.chdir(andrew['home'])

            # Create a label.
            name = "test_get_client_use_label_name"
            labelDict = {
                "label": name,
                "description": name,
                "view": "//depot/...",
            }
            p4.label(label=labelDict)
            self.failUnlessRaises(P4LibError, p4.client, name=name)
        finally:
            os.chdir(top)


def suite():
    """Return a unittest.TestSuite to be used by test.py."""
    return unittest.makeSuite(ClientTestCase)

