<template>
    <div id="login-app">
    <header>
            <nav>
                <a href="/" class="logo">
                    <img src="/src/assets/SELMTECH.png">
                </a>

                <div id="mySidebar" class="sidebar">
                    <a href="javascript:void(0)" class="closebtn"  ref="closebtn">&times;</a>
                            <a href="">Home</a>
                            <a href="">About</a>
                            <a href="">Services</a>
                </div>

                <div class="side-btn" id="side-b">
                    <button class="openbtn" ref="openbtn">&#9776;</button>

                </div>
            </nav>
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
export default{
    name: 'OpenNaV',
    mounted() {
    this.addClickListener();
    },
    methods: {
    addClickListener() {
    const elementopen = this.$refs.openbtn;
    const elementclose = this.$refs.closebtn;

    if (elementopen) {
        elementopen.addEventListener('click', this.handleOpenClick);
    };
    if (elementclose){
        elementclose.addEventListener('click', this.handleCloseClick);
    };
    },
    handleOpenClick() {
    this.$refs.sidebar.style.width = "250px";
    this.$refs.sideb.style.marginLeft = "250px"
    },
    handleCloseClick() {
    this.$refs.sidebar.style.width = "0px";
    this.$refs.sideb.style.marginLeft = "0px"
    }
    },

}
</script>