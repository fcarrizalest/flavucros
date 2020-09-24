<template>
	<fieldset>
		<legend>{{channel}}</legend>

		<ul>

		</ul>

		<textarea  v-model="newMsgText"></textarea>
		<button v-on:click="send">Enviar</button>
	</fieldset>
</template>

<script>
    export default {    
    	props: {
    	 	session:{
    	 		required: true
    	 	},
    	 	channel:{
    	 		required: true
    	 	}
    	},
    	watch: {
    		session(s){

    			console.log(this.channel);
    			let self = this;
    			s.subscribe('com.example.'+this.channel, function(args){
    				self.msgs = args;
    			});
    		}

    	},
    	mounted(){

    		console.log('Se muestra');
    	},
    	methods: {

    		send: function(event){
	  			let self = this;
	  			let chanel = this.channel

                axios.post('/msg',{ channel:chanel, msg:self.newMsgText}).then(function (response) {
                        // handle success
                        if(response.status == 200){
                            if(response.data.success){
                                
                            }
                        }
                        
                      })
                      .catch(function (error) {
                        // handle error
                        console.log(error);
                      })
                      .then(function () {
                        // always executed
                      });

				
			}
  		

    	},
    	data() {
            return {
            	msgs:[],
            	newMsgText:"Escribe el mensaje"
           //   chanel: '',
           }
        }
    }
</script>