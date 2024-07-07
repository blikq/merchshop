<template>
    <form id="form">
            <h3>REGISTER NOW</h3>
                Username:
                <input type="text" v-model="userData.username" name="username" class="input" required>

                Email:
                <input type="email" v-model="userData.email" name="email" class="input" required>

                <!-- Password:
                <input type="password" ref="password" v-model="userData.password" name="psw"  class="input email" required>

                Cofirm Password:
                <input type="password" ref="repassword" v-model="userData.repassword" name="psw"  class="input remail" required> -->
                <label for="password">Password:</label>
                <div class="pass-container">
                <input :class='{valid:passwordValidation.valid}' :type="passwordVisible ? 'text' : 'password'" v-model="userData.password" class="input email">
                <i id="eye-visibility" class="fa-solid fa-eye" tabindex='-1' @click='togglePasswordVisibility' :arial-label='passwordVisible ? "Hide password" : "Show password"'></i>
                </div>
                <label for="password">Confirm Password:</label>
                <input type="password" v-model.lazy='userData.checkPassword' class="input remail">

                <div class="matches" v-if='notSamePasswords'>
		            <p>Passwords don't match.</p>
	            </div>

                <div>
                    <button type="submit"    @click.prevent='resetPasswords' value="Sign Up">Sign Up</button>

                </div>
                <transition name="hint" appear>
                    <div v-if='passwordValidation.errors.length > 0 && !submitted' class='hints'>
                        <h2>Password Hints</h2>
                        <p v-for='error in passwordValidation.errors'>{{error}}</p>
                    </div>
                </transition>

                <div>
                    <p class="re-log">Already have an account? <a href="/login">Login</a></p>
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
      userData: { username: "", email: "", password: "", checkpassword: "" },
      rules: [
				{ message:'One lowercase letter required.', regex:/[a-z]+/ },
				{ message:"One uppercase letter required.",  regex:/[A-Z]+/ },
				{ message:"8 characters minimum.", regex:/.{8,}/ },
				{ message:"One number required.", regex:/[0-9]+/ }
			],
			password:'',
			checkPassword:'',
			passwordVisible:false,
			submitted:false
    };
  },
  components: {
      
  },
  
  methods: {

    userLogin() {
        console.log("lol");
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
    resetPasswords () {
        if (this.passwordValidation.valid && !this.notSamePasswords){
            this.userLogin();            
        }else{ 
            this.userData.password = ''
			this.userData.checkPassword = ''
        }
			this.submitted = true
			setTimeout(() => {
				this.submitted = false
			}, 2000)

		},
		togglePasswordVisibility () {
			this.passwordVisible = !this.passwordVisible
		}
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
        computed: {
		notSamePasswords () {
			if (this.passwordsFilled) {
				return (this.userData.password !== this.userData.checkPassword)
			} else {
				return false
			}
		},
		passwordsFilled () {
			return (this.userData.password !== '' && this.checkPassword !== '')
		},
		passwordValidation () {
			let errors = []
			for (let condition of this.rules) {
				if (!condition.regex.test(this.userData.password)) {
					errors.push(condition.message)
				}
			}
			if (errors.length === 0) {
                
				return { valid:true, errors }

			} else {
				return { valid:false, errors }
			}
		}

    }
};


</script>

<style>
@import '../assets/form.css';
@import '../assets/login.css';


</style>