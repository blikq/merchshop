
<template>
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
</template>

<script>
import { ref } from 'vue';

export default {
    
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
        }
        if (elementclose) {
            elementclose.addEventListener('click', this.handleCloseClick);
        }
        
    },
    handleOpenClick() {
        window.location.href = '';

        const sidebar = this.$refs.sidebar;
        const sideb = this.$refs.sideb;

        if (sidebar) {
            sidebar.style.width = "250px";
        }
        if (sideb) {
            sideb.style.marginLeft = "250px";
        }
    },
    handleCloseClick() {
        const sidebar = this.$refs.sidebar;
        const sideb = this.$refs.sideb;

        if (sidebar) {
            sidebar.style.width = "0px";
        }
        if (sideb) {
            sideb.style.marginLeft = "0px";
        }
    }
    },

}


</script>

<style>
@import '../assets/form.css';
@import '../assets/login.css';


</style>