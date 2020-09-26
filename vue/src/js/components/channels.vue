<template>
    <fieldset>
        <legend>Menu</legend>
        <ul>
        	 <li v-for="item in channels">
                <a href="#" v-on:click="select(item.id,item.name)"> {{item.name}}</a>
            </li>
        </ul>
       	<input v-model="newChannel" type="text" name="newChannel"/>
       	<button v-on:click="send">New Channel</button>
    </fieldset>
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