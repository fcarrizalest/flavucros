<template>
    <div class="w-full max-w-sm">
        <div class="flex mb-4">
          <div class="w-full h-12">
              <h2>Login</h2>
          </div>
        </div>
        <div class="md:flex md:items-center mb-6">
            <div class="md:w-1/3">
                <label class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4" for="inline-full-name">
                    Email
                </label>
            </div>
            <div class="md:w-2/3">
                <input v-model="email" name="email" class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" id="inline-full-name" type="text" value="Jane Doe">
            </div>
        </div>
        <div class="md:flex md:items-center mb-6">
            <div class="md:w-1/3">
                <label class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4" for="inline-password">
                    Password
                </label>
            </div>
            <div class="md:w-2/3">
                <input type="password" v-model="password"  class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" id="inline-password"  placeholder="******************">
            </div>
        </div>

        <div class="md:flex md:items-center">
            <div class="md:w-1/3"></div>
            <div class="md:w-2/3">
              <button class="shadow bg-purple-500 hover:bg-purple-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded" v-on:click="send" type="button">
                Login
            </button>
        </div>
    </div>
</div>
</template>

<script>
    export default {    
        props: {
            
        },
        
        methods: {

            send: function(event){
                let self = this;
                let chanel = this.channel
                
                axios.post('/login',{ email: this.email, password:this.password }).then(function (response) {
                        // handle success
                        if(response.status == 200){
                            if(response.data.success){
                                let token = response.data.token;
                                localStorage.setItem("auth_token", token);
                                self.$emit('login');
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
                email:"",
                password:""
           //   chanel: '',
           }
        }
    }
</script>