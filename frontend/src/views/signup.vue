<template>


    <header>
        <nav id="fnav">
            <a href="/" class="logo">
                <img src="/src/assets/SELMTECH.png">
            </a>

            <div id="mySidebar" class="sidebar" ref="sidebar">
                    <a href="javascript:void(0)" class="closebtn" ref="closebtn">&times;</a>
                            <a href="">Home</a>
                            <a href="">About</a>
                            <a href="">Services</a>
                </div>

    <div class="side-btn" id="side-b" ref="sideb">
                    <button class="openbtn" ref="openbtn">&#9776;</button>

                </div>

        </nav>
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