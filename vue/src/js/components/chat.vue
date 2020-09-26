<template>
	<fieldset>
		<legend>{{channel}}</legend>

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
    				if(args[1] == self.channelid){
                        self.msgs = args[0];
                    }
                    console.log(args)
    			});
    		},
            channelid(newValue,oldValue){

                
                this.msgs = [];
                this.updateMsg();
                let self = this;
                //this.session.unsubscribe('com.example.'+oldValue)
                this.session.subscribe('com.example.'+newValue, function(args){
                    if(args[1] == self.channelid){
                        self.msgs = args[0];
                    }
                    console.log(args)
                });

            }

    	},
    	mounted(){
            let self = this;
            self.updateMsg();
    	},
    	methods: {

            updateMsg:function(){
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
                        self.newMsgText= "";
                      });
			}
    	},
    	data() {
            return {
            	msgs:[],
            	newMsgText:"Escribe el mensaje"
                
           }
        }
    }
</script>