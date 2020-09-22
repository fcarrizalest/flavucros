import Vue from 'vue'
import axios from 'axios'

import Chat from './components/chat.vue'


window.axios = axios;

window.axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('auth_token'); 

window.axios.defaults.baseURL = 'http://localhost';

let dataInput = {
	session : null
}
const app = new Vue({
    el: '#app',
    data:dataInput,
    components:{Chat}
});




let connection = new autobahn.Connection({url: 'ws://localhost:8080/ws', realm: 'realm1'});
connection.onopen = function (session) {
	dataInput.session = session
};

connection.onclose = function (session) {
	dataInput.session = null
};

connection.open();