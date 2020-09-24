    <template>
    <fieldset>
        <legend>Login</legend>

        <div>
            <input type="text" v-model="email" name="email"/>
        </div>
        <div>
            <input type="password" v-model="password" name="password"/>
        </div>
        
        <button v-on:click="send">Login</button>
    </fieldset>
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