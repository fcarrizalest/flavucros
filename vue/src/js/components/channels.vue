<template>
  <div>

    <div class="w-full max-w-xs">
        <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
              New Channel
            </label>
            <input v-model="newChannel" type="text" name="newChannel" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"placeholder="Channel">
          </div>
          <div class="flex items-center justify-between">
            <button v-on:click="send" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
              New Channel
            </button>
            
          </div>
        </div>
      </div>

      <div class="mb-10">
        <a v-for="item in channels" v-on:click="select(item.id,item.name)" class="flex items-center px-2 -mx-2 py-1 hover:text-gray-900 font-medium text-gray-600">
            {{item.name}}
        </a>
      </div>
      
       
      </div>
       	
    
</template>
<script>
    export default {    
        methods: {
        	select:function(chanelId,channelName){
        		
        		console.log('click');
        		this.$emit('chanelchange',null,chanelId,channelName);
        	},
    		send: function(event){
	  			let self = this;
	  			let chanel = this.channel
                axios.post('/channels',{ name:self.newChannel}).then(function (response) {
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
    	mounted(){
            let self = this;

            axios.get('/channels').then(function (response) {
                        // handle success
                    if(response.status == 200){
                        if(response.data.success){

                        	console.log(response.data.data);
                            self.channels = response.data.data;
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
    	data() {
            return {
            	msgs:[],
            	newChannel:" ",
            	channels:[]
                
           }
        }
    }
</script>