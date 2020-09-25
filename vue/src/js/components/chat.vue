<template>
	<fieldset>
		<legend>{{channel}} {{channelid}}</legend>

		<ul>
            <li v-for="item in msgs">
                {{item.messages}}
            </li>
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
    	 	},
            channelid:{
                required:true
            }
    	},
    	watch: {
    		session(s){

    			console.log(this.channel);
    			let self = this;
    			s.subscribe('com.example.'+this.channelid, function(args){
    				self.msgs = args[0];
                    console.log(args)
    			});
    		}

    	},
    	mounted(){
            let self = this;
            axios.get('/channel/'+self.channelid+'/msg',{ msg:self.newMsgText}).then(function (response) {
                        // handle success
                    if(response.status == 200){
                        if(response.data.success){
                            self.msgs = response.data.data;
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
    		
    	},
    	methods: {

    		send: function(event){
	  			let self = this;
	  			let chanel = this.channel

                axios.post('/channel/'+self.channelid+'/msg',{ msg:self.newMsgText}).then(function (response) {
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