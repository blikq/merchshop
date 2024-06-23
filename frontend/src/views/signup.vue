<template>


    <header>
        <nav>
            <a href="/" class="logo">
                <img src="/src/assets/SELMTECH.png">
            </a>

            <div id="mySidebar" class="sidebar">
                    <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
                            <a href="">Home</a>
                            <a href="">About</a>
                            <a href="">Services</a>
                </div>

                <div class="side-btn" id="side-b">
                    <button class="openbtn" onclick="openNav()">&#9776;</button>

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

</script>