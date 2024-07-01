<template>
    <form id="form">
            <h3>REGISTER NOW</h3>
                Username:
                <input type="text" v-model="userData.username" name="username" class="input" required>

                Email:
                <input type="email" v-model="userData.email" name="email" class="input" required>

                Password:
                <input type="password" ref="password" v-model="userData.password" name="psw"  class="input email" required>

                Cofirm Password:
                <input type="password" ref="repassword" v-model="userData.repassword" name="psw"  class="input remail" required>
                <span id='message'></span>
                <div>
                    <button type="submit"  @click.prevent="userLogin()" value="Sign Up">Sign Up</button>
                    <p>Already have an account? <a href="/login">Login</a></p>
                </div>
        </form>
</template>

<script>
import axios from "axios";
import store from '@/store'; // Adjust the path accordingly


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export default {
  data() {
    return {
      userData: { username: "", email: "", password: "", repassword: "" },
    };
  },
  
  methods: {

    userLogin() {
      axios
        .post("/api/signup", this.userData ,{
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),  // Include CSRF token if needed
                'Access-Control-Allow-Origin': '*'
            }
        })
        .then((res) => {

            // this.$store.commit("SET_AUTH", true);
            // this.$store.commit("SET_TOKEN", res.data.token);
        //   this.$store.commit("SET_USER", res.data.employee);
          this.$router.push("/");
        });
    },
    // CheckPass() {
    //         if (this.$ref.password.value ==
    //         this.$ref.repassword.value) {
    //             this.$ref.message.style.color = 'green';
    //             this.$ref.message.innerHTML = 'matching';
    //         } else {
    //             this.$ref.message.style.color = 'red';
    //             this.$ref.message.innerHTML = 'not matching';
    //         }
    // }
},

};


</script>

<style>
@import '../assets/form.css';
@import '../assets/login.css';


</style>