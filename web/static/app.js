var data = {
	   title : "Chat",
	   status :'En Espera',
	   newMsgText: 'Escribe tu mensaje',
	   msgs:[]
	}

var vm = new Vue({
  el: '#app',
  data: data,
  methods: {
  		send: function(event){
  			var self = this;
			fetch('/msg', {
			   method: 'POST',
			   body: JSON.stringify({ msg:self.newMsgText})
			}).then(function(response) { 
				self.newMsgText = "";
			});
  		}
   }
})

var connection = new autobahn.Connection({url: 'ws://localhost:8080/ws', realm: 'realm1'});
connection.onopen = function (session) {

	console.log(data);

	data.status = 'conectado';
	function onevent(args) {
		data.msgs = args[0]
   	}
   	session.subscribe('com.example.msg', onevent);
};

connection.open();