from autobahn.twisted.component import Component, run
from autobahn.twisted.util import sleep
from twisted.internet.defer import inlineCallbacks
import os
import argparse
import six

url = u'ws://crossbar:8080/ws'
realmv = u'realm1'
print(url, realmv)
component = Component(transports=url, realm=realmv)

@component.on_join
@inlineCallbacks
def joined(session, details):
    print("session ready")
    counter = 0
    while True:
        # publish() only returns a Deferred if we asked for an acknowledgement
        session.publish(u'com.myapp.hello')
        counter += 1
        yield sleep(1)

if __name__ == "__main__":
    run([component])