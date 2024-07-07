<template>
               
</template>

<script>

export default{
	data () {
		return {
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
		}
	},
	methods: {
		resetPasswords () {
			this.password = ''
			this.checkPassword = ''
			this.submitted = true
			setTimeout(() => {
				this.submitted = false
			}, 2000)
		},
		togglePasswordVisibility () {
			this.passwordVisible = !this.passwordVisible
		}	
	},
	computed: {
		notSamePasswords () {
			if (this.passwordsFilled) {
				return (this.password !== this.checkPassword)
			} else {
				return false
			}
		},
		passwordsFilled () {
			return (this.password !== '' && this.checkPassword !== '')
		},
		passwordValidation () {
			let errors = []
			for (let condition of this.rules) {
				if (!condition.regex.test(this.password)) {
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
}
</script>