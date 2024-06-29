<template>


    <header>
        <NavControl />
    </header>

    <div class="signUp">
        <div class="img" id="img"></div>

        <form id="form">
            <h3>REGISTER NOW</h3>
                Username:
                <input type="text" name="username" class="input" required>

                Email:
                <input type="email" name="email" class="input" required>

                Password:
                <input type="password" name="psw" class="input email" required>

                Cofirm Password:
                <input type="password" name="psw" class="input remail" required>

                <div>
                    <input type="submit" value="Sign Up">
                    <p>Already have an account? <a href="/login">Login</a></p>
                </div>
        </form>
    </div>
</template>

<script>

import NavControl from '@/components/NavControl.vue';

export default{
    name: "Signup",
    components: {
        NavControl
    }
}
   

</script>