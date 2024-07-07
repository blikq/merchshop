<template>
    <link rel="stylesheet" href="/src/assets/form.css">
    <link rel="stylesheet" href="/src/assets/login.css">

    <header>
        <NavControl />
    </header>

    <div class="signUp">
        <div class="img" id="img"></div>
        <SignupControl />
        
    </div>
</template>

<script>

import NavControl from '@/components/NavControl.vue';
import SignupControl from '@/components/SignupControl.vue';

export default{
    name: "Signup",
    components: {
        NavControl,
        SignupControl,
    }
}
   

</script>