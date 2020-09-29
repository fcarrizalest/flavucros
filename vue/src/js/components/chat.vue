<template>
    <div class="box-border bg-white p-4 border-4 border-gray-400 w-full  h-full m-1">
    <div class="grid grid-cols-6 gap-4">
        <div class="overflow-auto col-span-6 bg-white h-64">

            <p v-for="item in msgs" class="flex items-center px-2  py-1 hover:text-gray-900  text-gray-600">
                {{item.created}}        {{item.messages}}
            </p>

        </div>

        <div class="col-span-6 bg-white  h-12">

            <div class="grid grid-cols-6 gap-4">

                <div class="col-span-5">
                    <textarea  class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" v-model="newMsgText"></textarea>
                </div>
                <div class="col-span-1">
                    <button class="shadow bg-purple-500 hover:bg-purple-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded" v-on:click="send">Enviar</button>
                </div>
            </div>
            

            

        </div>
    </div>
</div>
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