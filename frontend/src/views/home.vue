<template>
    <h1> wassupu </h1>
    <p> hi {{ userData.username }} </p>
    
</template>

<script>
import axios from "axios";


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export default {
        data() {
        return {
            userData: { username: "",},
        };
    },
    beforeMount() {
        this.Authenticate();
    },
    methods: {
        Authenticate(){
                const token = this.$cookies.get('token'); console.log(token);
                const csrftoken = this.$cookies.get('csrf_token');
                axios
            .get("/api/test", this.userData ,{
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,  // Include CSRF token if needed
                    'Access-Control-Allow-Origin': '*',
                    'Authorization': 'token ' + token
                }
            })
            .then((res) => {
                console.log(res.data)
                this.userData.username = res.data.username
                console.log("good");
            });
        }
        },
    };
</script>