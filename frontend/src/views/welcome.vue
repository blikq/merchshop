<template>
    <link rel="stylesheet" href="/src/assets/ham.css">

    <header class="header">
                <!-- Logo -->
                <a href="#" class="logo">GEONET</a>
                <!-- Hamburger Icon -->
                <input class="side-menu" type="checkbox" id="side-menu">
                <label class="hamb" for="side-menu"><span class="hamb-line"></span></label>
                <!-- Menu -->
                <nav class="navbar">
                    <ul class="nav-menu">
                        <li class="nav-item"><a href="" class="nav-link">How it Works</a></li>
                        <li class="nav-item"><a href="" class="nav-link">Team Solutions</a></li>
                        <li class="nav-item"><a href="" class="nav-link">Creator Merch</a></li>
                        <li class="nav-item"><a href="" class="nav-link">Success Stories</a></li>
                        <li class="nav-item"><a href="" class="nav-link">Pricing</a></li>
                        <li class="nav-item"><a href="" class="nav-link">Lookbook</a></li>
                        <li class="nav-item"><a href="" class="nav-link">Login</a></li>
                        <button class="btn">Start a Project</button>
                    </ul>
                </nav>
    </header>

    <div class="hero">
        <div class="container" data-aos="fade-down">
            <h1>FASHION SOLUTIONS</h1>
            <p>Merch, swag and gifts for the modern business</p>
            <a class="btn" href="">How it Works</a>
            <a class="btn" href="">Get Started</a>
        </div>
    </div>
</template>

<script>
        AOS.init({
            disable: function() { var maxWidth = 768; return window.innerWidth < maxWidth; },
            duration: 600,
            easing: "linear",
        });
</script>