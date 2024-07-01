<template>
    <form id="form">
                <h3>LOGIN</h3>
                    Email:
                    <input type="text email" v-model="userData.email" name="email" class="input" required>

                    Password:
                    <input type="password" v-model="userData.password" name="psw" class="input remail" required>

                    <div>
                        <button type="submit" @click.prevent="userLogin()" ref="submit" value="login">Login</button>
                        <p>Don't have an account? <a href="/signup">Sign Up</a></p>
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
      userData: { password: "", email: "" },
    };
  },
  methods: {
    userLogin() {
      axios
        .post("/api/login", this.userData ,{
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
},

};


</script>

<style>
@import '../assets/form.css';
@import '../assets/login.css';


</style>