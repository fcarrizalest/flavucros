import jinja2
import json

import sqlalchemy
import bcrypt
import validators
import jwt
import datetime

from klein import Klein
from twisted.web.static import File
from twisted.internet.defer import inlineCallbacks, returnValue
from autobahn.twisted.wamp import Application

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine('mysql://root:root@mysql/flavucros')

Session = sessionmaker()

Session.configure(bind=engine)

session = Session()

Base = declarative_base()

class JsonSerializer(object):
    """A mixin that can be used to mark a SQLAlchemy model class which
    implements a :func:`to_json` method. The :func:`to_json` method is used
    in conjuction with the custom :class:`JSONEncoder` class. By default this
    mixin will assume all properties of the SQLAlchemy model are to be visible
    in the JSON output. Extend this class to customize which properties are
    public, hidden or modified before being being passed to the JSON serializer.
    """

    __json_public__ = None
    __json_hidden__ = None
    __json_modifiers__ = None

    def get_field_names(self):
        for p in self.__mapper__.iterate_properties:
            yield p.key

    def to_json(self):
        field_names = self.get_field_names()

        public = self.__json_public__ or field_names
        hidden = self.__json_hidden__ or []
        modifiers = self.__json_modifiers__ or dict()

        rv = dict()
        for key in public:
            rv[key] = getattr(self, key)
            if isinstance(rv[key], datetime.datetime):
                rv[key] = rv[key].__str__()
        for key, modifier in modifiers.items():
            value = getattr(self, key)
            rv[key] = modifier(value, self)
        for key in hidden:
            rv.pop(key, None)
        return rv

class User(Base,JsonSerializer):
    __tablename__ = 'users'
    __json_public__ = ['id','email']

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(email='%s' id='%s')>" % (self.email,self.id)

class Channel(Base,JsonSerializer):
    __tablename__ = 'channels'
    __json_public__ = ['id','name','description']

    id = Column(Integer,primary_key=True)
    name = Column(String)
    user_id = Column(Integer)
    description = Column(String)


class Msg(Base,JsonSerializer):
    __tablename__ = 'channel_messages'
    __json_public__ = ['id','channel_id', 'messages','created']

    id = Column(Integer,primary_key=True)
    channel_id = Column(Integer)
    user_id = Column(Integer,ForeignKey('users.id'))
    messages = Column(String)
    created = Column(String)
    #user = relationship("User", back_populates="msgs")



# ed_user = User(email='fcarrizales@gmail')
# session.add(ed_user)
# session.commit()


# This is our WAMP application
##
wampapp = Application('com.example')


# This is our Web application
##
webapp = Klein()
webapp.visits = 0
webapp.msgs = [];
webapp.templates = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


def valid_user(user):
    messages = []
    if not validators.email(user['email']):
        messages.append('Error email')

    return messages

@webapp.route('/static/', branch=True)
def static(request):
    return File("./static")

@webapp.route('/channels', methods=['POST'])
def do_new_channel(request):
    content = json.loads(request.content.read())
    error = False
    msg = ""
    success = False

    tokens = request.requestHeaders.getRawHeaders('authorization')
    
    try:
        tokens = tokens[0].split(' ')
        token = tokens[1]
        public_key = open('id_rsa.pub').read()
        payload = jwt.decode(token, public_key, algorithms=['RS256'])
        print('tengo el token se quien eres ')
        print(payload)

        msgNew = Channel(name=content['name'],user_id=payload['id'],description=content['name'])
        session.add(msgNew)
        session.commit()

        rows = session.query(Channel).limit(100).all()

        ms = []
        for row in rows:
            ms.append(row.to_json())

        wampapp.session.publish('com.example.new_channel', ms )
        success=True

        
    except jwt.exceptions.InvalidTokenError :
        success = False
        msg = "TOKEN ERROR"

    

    response = json.dumps(dict(error=error, msg=msg, success=success), indent=4)
    return response

@webapp.route('/channels', methods=['GET'])
def list_channels(request):
    error = False
    msg = ""
    success = False

    tokens = request.requestHeaders.getRawHeaders('authorization')
    data = []
    try:
        tokens = tokens[0].split(' ')
        token = tokens[1]
        public_key = open('id_rsa.pub').read()
        payload = jwt.decode(token, public_key, algorithms=['RS256'])
        print('tengo el token se quien eres ')
        print(payload)

        rows = session.query(Channel).limit(100).all()
        
        for row in rows:
            data.append(row.to_json())

        success=True

        
    except jwt.exceptions.InvalidTokenError :
        success = False
        msg = "TOKEN ERROR"

    

    response = json.dumps(dict(data=data, error=error, msg=msg, success=success), indent=4)
    return response


@webapp.route('/channel/<string:chid>/msg', methods=['GET'])
def do_list_channel(request,chid):
    
    error = False
    msg = ""
    success = False
    data = []
    tokens = request.requestHeaders.getRawHeaders('authorization')
    
    try:
        tokens = tokens[0].split(' ')
        token = tokens[1]
        public_key = open('id_rsa.pub').read()
        payload = jwt.decode(token, public_key, algorithms=['RS256'])
        print('tengo el token se quien eres ')
        print(payload)

        rows = session.query(Msg).filter(Msg.channel_id==chid).limit(100).all()
        data = []
        for row in rows:
            data.append(row.to_json())

        #wampapp.session.publish('com.example.%s' % (chid), ms )
        success=True

        
    except jwt.exceptions.InvalidTokenError :
        success = False
        msg = "TOKEN ERROR"

    

    response = json.dumps(dict(error=error,data=data, msg=msg, success=success), indent=4)
    return response

@webapp.route('/channel/<string:chid>/msg', methods=['POST'])
def do_new_post(request,chid):
    content = json.loads(request.content.read())
    error = False
    msg = ""
    success = False

    tokens = request.requestHeaders.getRawHeaders('authorization')
    
    try:
        tokens = tokens[0].split(' ')
        token = tokens[1]
        public_key = open('id_rsa.pub').read()
        payload = jwt.decode(token, public_key, algorithms=['RS256'])
        print('tengo el token se quien eres ')
        print(payload)

        msgNew = Msg(channel_id=chid,user_id=payload['id'],messages=content["msg"])
        session.add(msgNew)
        session.commit()

        rows = session.query(Msg).filter(Msg.channel_id==chid).limit(100).all()

        ms = []
        for row in rows:
            ms.append(row.to_json())

        wampapp.session.publish('com.example.%s' % (chid), ms, chid )
        success=True

        
    except jwt.exceptions.InvalidTokenError :
        success = False
        msg = "TOKEN ERROR"

    

    response = json.dumps(dict(error=error, msg=msg, success=success), indent=4)
    return response


@webapp.route('/login', methods=['POST'])
def do_login(request):
    content = json.loads(request.content.read())
    row =session.query(User).filter_by( email = content['email'] ).one_or_none()
    error = False
    msg = "KO"
    token = ""
    success = True



    if row is not None and  bcrypt.checkpw(content['password'].encode('utf8'), row.password.encode('utf8') ) :
        private_key = open('id_rsa').read()
        msg = 'OK'
        user = dict(id=row.id, email=row.email)
        user['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        token = jwt.encode(user , private_key, algorithm='RS256').decode('utf-8')
        success=True
    else:
        msg = "Email o password incorrectos"
        success=False



    response = json.dumps(dict(error=error, msg=msg,token=token,success=success), indent=4)
    return response



@webapp.route('/register', methods=['POST'])
def do_register(request):
    content = json.loads(request.content.read())
    msg = "KO"
    error = False
    success = False
    if content['email'] and content['password'] :
        row =session.query(User).filter_by( email = content['email'] ).one_or_none()
        if row is None:
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(content['password'].encode('utf8') , salt)
            if isinstance(hashed, str):
                password = hashed
            else:
                password = hashed.decode("UTF-8") 

            ed_user = User(email=content['email'],password=password)
            session.add(ed_user)
            session.commit()
            msg = "Usuario Registrado"
            success = True
        else: 
            error = "Correo ya Existe"
            success = False

    response = json.dumps(dict(error=error, msg=msg, success=success), indent=4)
    return response





@webapp.route('/check', methods=['POST'])
def do_check(request):
    pass

@webapp.route('/msg', methods=['POST'])
def do_post(request):
    content = json.loads(request.content.read())

    token = request.requestHeaders.getRawHeaders('authorization')

    webapp.msgs.append( dict( text=content["msg"] ) )
    wampapp.session.publish('com.example.msg', webapp.msgs )
    response = json.dumps(dict(the_data=content), indent=4)
    return response

@webapp.route('/')
def home(request):
    webapp.visits += 1
    wampapp.session.publish('com.example.msg', webapp.msgs)
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