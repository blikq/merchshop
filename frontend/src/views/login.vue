<template>
    <link rel="stylesheet" href="/src/assets/form.css">
    <link rel="stylesheet" href="/src/assets/login.css">
    <div id="login-app">
    <header>
            <NavControl />
        </header>

        <div class="signUp">
            <div class="img" id="img"></div>

            <LoginControl />
        </div>
        </div>
</template>

<script>
import NavControl from '@/components/NavControl.vue';
import LoginControl from '@/components/LoginControl.vue';

export default{
    name: "Login",
    components: {
        NavControl,
        LoginControl
    }
}
    

</script>