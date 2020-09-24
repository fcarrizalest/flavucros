import Vue from 'vue'
import axios from 'axios'

import Chat from './components/chat.vue'
import Register from './components/register.vue'
import Login from './components/login.vue'


window.axios = axios;

window.axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('auth_token'); 

window.axios.defaults.baseURL = 'http://localhost:5000';

let dataInput = {
	session : null,
	islogin:false,
	channelid:1,
	channelname:"Bienvenida"
}
const app = new Vue({
    el: '#app',
    data:dataInput,
    components:{Chat,Register,Login},
    methods:{
    	check : function(e){
    		let token = localStorage.getItem('auth_token');
    		if (token) {
	            let exp = this.getExpFromToken(token);
	            let time = new Date();
	            let now = Math.floor(time.getTime() / 1000);
	            if (now > exp) {
	                this.islogin =false;
	            }else{
	            	this.islogin = true;
					axios.defaults.headers.common['Authorization'] = 'Bearer ' + token; 
					
	        	}
        	}
    	},
    	getExpFromToken:function(jwtBearer) {
	        let exp = 0;
	        if (jwtBearer) {
	            let jwt = jwtBearer.split('.');
	            if (jwt.length == 3) {
	                let expObj = JSON.parse(atob(jwt[1]));
	                exp = expObj.exp;
	            }
	        }
	        return exp;
	    }

    },
    mounted(){
    	let self = this;
    	setInterval(function(){
            self.check();
        }, 600000);
        self.check();
    }
});




let connection = new autobahn.Connection({url: 'ws://localhost:8080/ws', realm: 'realm1'});
connection.onopen = function (session) {
	dataInput.session = session
};

connection.onclose = function (session) {
	dataInput.session = null
};

connection.open();