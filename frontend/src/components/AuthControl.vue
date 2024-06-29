<script>
import { mapActions, mapGetters } from 'vuex'

export Auth {
data: () => ({
    user: {
    username: null,
    password: null
    }
}),
computed: {
    ...mapGetters({
    authUser: 'auth/user'
    })
},
methods: {
    ...mapActions({
    loginUser: 'auth/loginUser'
    }),
    async login() {
    await this.loginUser(this.user)
        .then(() => {
        if (this.authUser.authenticated) {
            this.$router.push('/secure')
        } else {
            // Handle error
            this.user = {
            username: null,
            password: null
            }
        }
        })
    
    }
}
}

</script>