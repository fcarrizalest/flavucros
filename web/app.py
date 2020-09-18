import jinja2
from klein import Klein

from twisted.internet.defer import inlineCallbacks, returnValue
from autobahn.twisted.wamp import Application


# This is our WAMP application
##
wampapp = Application('com.example')


# This is our Web application
##
webapp = Klein()
webapp.visits = 0
webapp.templates = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


@webapp.route('/')
def home(request):
    webapp.visits += 1
    wampapp.session.publish('com.example.onvisit', webapp.visits)
    page = webapp.templates.get_template('index.html')
    return page.render(visits=webapp.visits)



if __name__ == "__main__":
    import sys
    from twisted.python import log
    from twisted.web.server import Site
    from twisted.internet import reactor
    log.startLogging(sys.stdout)

    reactor.listenTCP(5000, Site(webapp.resource()))
    wampapp.run("ws://crossbar:8080/ws", "realm1")