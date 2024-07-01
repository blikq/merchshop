<template>
    <h1> wassupu </h1>

    
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
        beforeMount() {
            this.Authenticate();
        },
        methods: {
            Authenticate(){
                axios
            .get("/api/test", this.userData ,{
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),  // Include CSRF token if needed
                    'Access-Control-Allow-Origin': '*',
                    'Authorization': 'token ' + getCookie('token')
                }
            })
            .then((res) => {
                console.log("good");
            });
        }
        },
    };
</script>