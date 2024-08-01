<template>
    <form id="form">
            <h3>REGISTER NOW</h3>
                Username:
                <input type="text" v-model="userData.username" name="username" class="input" required>

                Email:
                <div class="pass-container">

                    <input type="email" v-model="userData.email" name="email" class="input" required>
                    <!-- <i id="pin-reload" class="fa fa-refresh" tabindex='-1' ></i> -->
                    <div class="getty" ref="getcode">Get Code</div>
                
                </div>
                <p id="validationMessage">{{ validation }}</p>
                <br>
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
                <input type="password" v-model.lazy='passwordHandler.checkpassword' class="input remail">

                <label for="pin">Email Pin:</label>
                    <input type="text" name="pin" v-model="pin.pin" class="input email">

                
                
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

//Valid Email?
function validateEmail(emailInput, validation) {
    // const validationMessage = document.getElementById("validationMessage");
    const email = emailInput;
    console.log(email)
    // Check if email is empty
    if (email === "") {
        validationMessage.innerText = "Please enter an email address";
        return false;
    }

    // Check if email is valid
    const emailParts = email.split("@");
    if (emailParts.length !== 2) {
        validationMessage.innerText = "Please enter a valid email address - missing or too many '@' symbols";
        return false;
    }

    const localPart = emailParts[0];
    const domainPart = emailParts[1];

    // Check local part for invalid characters
    const localPartRegex = /^[a-zA-Z0-9!#$%&'*+\-/=?^_`{|}~]+(\.[a-zA-Z0-9!#$%&'*+\-/=?^_`{|}~]+)*$/;
    if (!localPartRegex.test(localPart)) {
        validationMessage.innerText = "Please enter a valid email address - invalid characters in local part";
        return false;
    }

    // Check local part for consecutive periods
    if (localPart.includes("..")) {
        validationMessage.innerText = "Please enter a valid email address - consecutive periods in local part";
        return false;
    }

    // Check local part for leading or trailing period
    if (localPart.startsWith(".") || localPart.endsWith(".")) {
        validationMessage.innerText = "Please enter a valid email address - leading or trailing period in local part";
        return false;
    }

    // Check domain part for invalid characters
    const domainPartRegex = /^[a-zA-Z0-9.-]+$/;
    if (!domainPartRegex.test(domainPart)) {
        validationMessage.innerText = "Please enter a valid email address - invalid characters in domain part";
        return false;
    }

    // Check domain part for consecutive hyphens
    if (domainPart.includes("--")) {
        validationMessage.innerText = "Please enter a valid email address - consecutive hyphens in domain part";
        return false;
    }

    // Check domain part for leading or trailing hyphen
    if (domainPart.startsWith("-") || domainPart.endsWith("-")) {
        validationMessage.innerText = "Please enter a valid email address - leading or trailing hyphen in domain part";
        return false;
    }

    // Check domain part for valid TLD
    const tldRegex = /^[a-zA-Z]{2,}$/;
    const domainParts = domainPart.split(".");
    if (domainParts.length < 2 || !tldRegex.test(domainParts[domainParts.length - 1])) {
        validationMessage.innerText = "Please enter a valid email address - invalid top-level domain";
        return false;
    }

    // Email is valid
    validationMessage.innerText = "";
    return true;
}

export default {
  data() {
    return {
      userData: { username: "", email: "", password: ""},
      pin: {pin: ""},
      passwordHandler: {checkpassword: ""},
      rules: [
				{ message:'One lowercase letter required.', regex:/[a-z]+/ },
				{ message:"One uppercase letter required.",  regex:/[A-Z]+/ },
				{ message:"8 characters minimum.", regex:/.{8,}/ },
				{ message:"One number required.", regex:/[0-9]+/ }
			],

			passwordVisible:false,
			submitted:false,
            validation: "",
            
    
        };
    },
    components: {
      
    },
    mounted() {
        this.addClickListener();
    },
  
  methods: {

    userLogin() {
        console.log("lol");
      axios
        .post("/api/signup", this.userData ,{
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),  // Include CSRF token if needed
                'Access-Control-Allow-Origin': '*',
                'pin': this.pin.pin,
            }
        })
        .then((res) => {
            this.$router.push("/");
        }).catch((err) => {
            console.error(err);
        });
    },
    resetPasswords () {
        if (this.passwordValidation.valid && !this.notSamePasswords){
            this.userLogin();            
        }else{ 
            this.userData.password = ''
			this.passwordHandler.checkpassword = ''
        }
			this.submitted = true
			setTimeout(() => {
				this.submitted = false
			}, 2000)

	},

    togglePasswordVisibility () {
        this.passwordVisible = !this.passwordVisible
    },

    addClickListener() {
        const getcode = this.$refs.getcode;
        if (getcode) {
            getcode.addEventListener('click', this.clickedGetEmail);
        }
    },

    clickedGetEmail() {
        const valid = validateEmail(this.userData.email, this.validation);
        const intake = {
            email: this.userData.email,
        }
            if (valid) {
                axios
                .post("/api/verify_email", intake ,{
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken'),  // Include CSRF token if needed
                        'Access-Control-Allow-Origin': '*'
                    }
                })
            .then((res) => {
                // console.log(res)
                if (res.data.time_left) {
                    
                    alert("try agin in " + res.data.time_left + " seconds")
                }else {
                    alert("code sent")
                }
            }).catch((err) => {
                

            });
        }
    },
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
				return (this.userData.password !== this.passwordHandler.checkpassword)
			} else {
				return false
			}
		},
		passwordsFilled () {
			return (this.userData.password !== '' && this.passwordHandler.checkpassword !== '')
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