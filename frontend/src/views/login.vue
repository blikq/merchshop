<template>
    <div id="login-app">
    <header>
            <NavControl />
        </header>

        <div class="signUp">
            <div class="img" id="img"></div>

            <form id="form">
                <h3>LOGIN</h3>
                    Username/Email:
                    <input type="text email" name="email" class="input" required>

                    Password:
                    <input type="password" name="psw" class="input remail" required>

                    <div>
                        <input type="submit" value="Login">
                        <p>Don't have an account? <a href="/signup">Sign Up</a></p>
                    </div>
            </form>
        </div>
        </div>
</template>

<script>
import NavControl from '@/components/NavControl.vue';

export default{
    name: "Login",
    components: {
        NavControl
    }
}
    

</script>