<template>
<!DOCTYPE html>
<html lang="en">

<body onload="short()">
    <div id="login-app">
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

</body>

</html>
</template>

<script>
</script>