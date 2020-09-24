<template>
    <fieldset>
        <legend>Register</legend>

        <div>
            <input type="text" v-model="email" name="email"/>
        </div>
        <div>
            <input type="password" v-model="password" name="password"/>
        </div>
        
        <button v-on:click="send">Register</button>
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
                
                window.axios.post('/register',{ email: this.email, password:this.password }).then( function(e){

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