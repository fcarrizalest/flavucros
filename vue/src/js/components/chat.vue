<template>
	<fieldset>
		<legend>{{channel}}</legend>

		<ul>
            <li v-for="item in msgs">
                {{item.messages}}
            </li>
		</ul>

        <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 md:flex md:items-center mb-6 ">
            <div class="md:w-2/3">
        		<textarea  class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" v-model="newMsgText"></textarea>
            </div>
              <div class="md:w-1/3">
		<button class="shadow bg-purple-500 hover:bg-purple-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded" v-on:click="send">Enviar</button>
    </div>
        </div>
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