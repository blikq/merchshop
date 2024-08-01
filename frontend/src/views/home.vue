<template>
<!--
// v0 by Vercel.
// https://v0.dev/t/IJAJAZFr9vG
-->

<div class="bg-background text-foreground">
  <header class="flex items-center justify-between px-4 py-3 border-b border-muted">
    <div class="text-2xl font-bold">
      <a href="#">Selmtech</a>
    </div>
    <div class="flex items-center gap-2">
      <div class="relative w-full max-w-[300px]">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground"
        >
          <circle cx="11" cy="11" r="8"></circle>
          <path d="m21 21-4.3-4.3"></path>
        </svg>
        <input
          class="flex h-10 rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 pl-8 w-full"
          type="search"
          placeholder="Search products..."
        />
      </div>
      <div class="flex items-center gap-2 ml-4 sm:ml-0">
        <button class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-10 px-2 py-1 sm:px-4 sm:py-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="w-5 h-5 mr-2 hidden sm:block"
          >
            <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
            <polyline points="10 17 15 12 10 7"></polyline>
            <line x1="15" x2="3" y1="12" y2="12"></line>
          </svg>
          <span class="text-sm sm:text-base">Sign In</span>
        </button>
        <button class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-10 px-2 py-1 sm:px-4 sm:py-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="w-5 h-5 mr-2 hidden sm:block"
          >
            <circle cx="8" cy="21" r="1"></circle>
            <circle cx="19" cy="21" r="1"></circle>
            <path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"></path>
          </svg>
          <span class="text-sm sm:text-base">Cart</span>
        </button>
      </div>
    </div>
  </header>
  <main class="container mx-auto py-12">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 px-4 md:px-6">
      <div class="bg-card rounded-lg overflow-hidden">
        <img
          src="/src/assets/SELMTECH.png"
          alt="Product 1"
          width="300"
          height="300"
          class="w-full h-48 sm:h-64 object-cover"
          style="aspect-ratio:300/300;object-fit:cover"
        />
        <div class="p-4 sm:p-6">
          <h3 class="text-lg sm:text-xl font-semibold mb-2">Wireless Headphones</h3>
          <p class="text-muted-foreground mb-4 line-clamp-2">
            Experience the ultimate in audio quality and comfort.
          </p>
          <div class="flex items-center justify-between">
            <span class="text-2xl font-bold">$99.99</span>
            <div class="block sm:hidden">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-9 rounded-md px-3">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-card rounded-lg overflow-hidden">
        <img
          src="/src/assets/SELMTECH.png"
          alt="Product 2"
          width="300"
          height="300"
          class="w-full h-48 sm:h-64 object-cover"
          style="aspect-ratio:300/300;object-fit:cover"
        />
        <div class="p-4 sm:p-6">
          <h3 class="text-lg sm:text-xl font-semibold mb-2">Wireless Earbuds</h3>
          <p class="text-muted-foreground mb-4 line-clamp-2">Experience true wireless freedom.</p>
          <div class="flex items-center justify-between">
            <span class="text-2xl font-bold">$79.99</span>
            <div class="block sm:hidden">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-9 rounded-md px-3">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-card rounded-lg overflow-hidden">
        <img
          src="/src/assets/SELMTECH.png"
          alt="Product 3"
          width="300"
          height="300"
          class="w-full h-48 sm:h-64 object-cover"
          style="aspect-ratio:300/300;object-fit:cover"
        />
        <div class="p-4 sm:p-6">
          <h3 class="text-lg sm:text-xl font-semibold mb-2">Noise-Cancelling Headphones</h3>
          <p class="text-muted-foreground mb-4 line-clamp-2">
            Block out the world and immerse yourself in your music.
          </p>
          <div class="flex items-center justify-between">
            <span class="text-2xl font-bold">$149.99</span>
            <div class="block sm:hidden">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-9 rounded-md px-3">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-card rounded-lg overflow-hidden">
        <img
          src="/src/assets/SELMTECH.png"
          alt="Product 4"
          width="300"
          height="300"
          class="w-full h-48 sm:h-64 object-cover"
          style="aspect-ratio:300/300;object-fit:cover"
        />
        <div class="p-4 sm:p-6">
          <h3 class="text-lg sm:text-xl font-semibold mb-2">Bluetooth Speaker</h3>
          <p class="text-muted-foreground mb-4 line-clamp-2">Bring the party wherever you go.</p>
          <div class="flex items-center justify-between">
            <span class="text-2xl font-bold">$59.99</span>
            <div class="block sm:hidden">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-9 rounded-md px-3">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-card rounded-lg overflow-hidden">
        <img
          src="/src/assets/SELMTECH.png"
          alt="Product 5"
          width="300"
          height="300"
          class="w-full h-48 sm:h-64 object-cover"
          style="aspect-ratio:300/300;object-fit:cover"
        />
        <div class="p-4 sm:p-6">
          <h3 class="text-lg sm:text-xl font-semibold mb-2">Smart Home Hub</h3>
          <p class="text-muted-foreground mb-4 line-clamp-2">Control your smart home devices with ease.</p>
          <div class="flex items-center justify-between">
            <span class="text-2xl font-bold">$99.99</span>
            <div class="block sm:hidden">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-9 rounded-md px-3">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-card rounded-lg overflow-hidden">
        <img
          src="/src/assets/SELMTECH.png"
          alt="Product 6"
          width="300"
          height="300"
          class="w-full h-48 sm:h-64 object-cover"
          style="aspect-ratio:300/300;object-fit:cover"
        />
        <div class="p-4 sm:p-6">
          <h3 class="text-lg sm:text-xl font-semibold mb-2">Fitness Tracker</h3>
          <p class="text-muted-foreground mb-4 line-clamp-2">Stay motivated and track your fitness goals.</p>
          <div class="flex items-center justify-between">
            <span class="text-2xl font-bold">$49.99</span>
            <div class="block sm:hidden">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-9 rounded-md px-3">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-card rounded-lg overflow-hidden">
        <img
          src="/src/assets/SELMTECH.png"
          alt="Product 7"
          width="300"
          height="300"
          class="w-full h-48 sm:h-64 object-cover"
          style="aspect-ratio:300/300;object-fit:cover"
        />
        <div class="p-4 sm:p-6">
          <h3 class="text-lg sm:text-xl font-semibold mb-2">Wireless Charging Pad</h3>
          <p class="text-muted-foreground mb-4 line-clamp-2">Charge your devices without the hassle of cables.</p>
          <div class="flex items-center justify-between">
            <span class="text-2xl font-bold">$29.99</span>
            <div class="block sm:hidden">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-9 rounded-md px-3">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-card rounded-lg overflow-hidden">
        <img
          src="/src/assets/SELMTECH.png"
          alt="Product 8"
          width="300"
          height="300"
          class="w-full h-48 sm:h-64 object-cover"
          style="aspect-ratio:300/300;object-fit:cover"
        />
        <div class="p-4 sm:p-6">
          <h3 class="text-lg sm:text-xl font-semibold mb-2">Smart Thermostat</h3>
          <p class="text-muted-foreground mb-4 line-clamp-2">Effortlessly control the temperature in your home.</p>
          <div class="flex items-center justify-between">
            <span class="text-2xl font-bold">$99.99</span>
            <div class="block sm:hidden">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-9 rounded-md px-3">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-card rounded-lg overflow-hidden">
        <img
          src="/src/assets/SELMTECH.png"
          alt="Product 9"
          width="300"
          height="300"
          class="w-full h-48 sm:h-64 object-cover"
          style="aspect-ratio:300/300;object-fit:cover"
        />
        <div class="p-4 sm:p-6">
          <h3 class="text-lg sm:text-xl font-semibold mb-2">Smartwatch</h3>
          <p class="text-muted-foreground mb-4 line-clamp-2">Stay connected and track your fitness.</p>
          <div class="flex items-center justify-between">
            <span class="text-2xl font-bold">$199.99</span>
            <div class="block sm:hidden">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-9 rounded-md px-3">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-card rounded-lg overflow-hidden">
        <img
          src="/src/assets/SELMTECH.png"
          alt="Product 10"
          width="300"
          height="300"
          class="w-full h-48 sm:h-64 object-cover"
          style="aspect-ratio:300/300;object-fit:cover"
        />
        <div class="p-4 sm:p-6">
          <h3 class="text-lg sm:text-xl font-semibold mb-2">Tablet</h3>
          <p class="text-muted-foreground mb-4 line-clamp-2">Enjoy entertainment and productivity on the go.</p>
          <div class="flex items-center justify-between">
            <span class="text-2xl font-bold">$299.99</span>
            <div class="block sm:hidden">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-9 rounded-md px-3">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-card rounded-lg overflow-hidden">
        <img
          src="/src/assets/SELMTECH.png"
          alt="Product 11"
          width="300"
          height="300"
          class="w-full h-48 sm:h-64 object-cover"
          style="aspect-ratio:300/300;object-fit:cover"
        />
        <div class="p-4 sm:p-6">
          <h3 class="text-lg sm:text-xl font-semibold mb-2">Laptop</h3>
          <p class="text-muted-foreground mb-4 line-clamp-2">Powerful performance for work and play.</p>
          <div class="flex items-center justify-between">
            <span class="text-2xl font-bold">$799.99</span>
            <div class="block sm:hidden">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-9 rounded-md px-3">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-card rounded-lg overflow-hidden">
        <img
          src="/src/assets/SELMTECH.png"
          alt="Product 12"
          width="300"
          height="300"
          class="w-full h-48 sm:h-64 object-cover"
          style="aspect-ratio:300/300;object-fit:cover"
        />
        <div class="p-4 sm:p-6">
          <h3 class="text-lg sm:text-xl font-semibold mb-2">Drone</h3>
          <p class="text-muted-foreground mb-4 line-clamp-2">Capture stunning aerial footage.</p>
          <div class="flex items-center justify-between">
            <span class="text-2xl font-bold">$499.99</span>
            <div class="block sm:hidden">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-9 rounded-md px-3">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="bg-card rounded-lg overflow-hidden mt-8 sm:mt-12 lg:mt-16">
      <div class="p-6 sm:p-8">
        <h2 class="text-2xl sm:text-3xl font-bold mb-4">Categories</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <div class="bg-muted text-foreground rounded-lg p-6 flex flex-col items-start justify-between hover:bg-accent hover:text-accent-foreground transition-colors">
            <div class="flex items-center gap-4 mb-4">
              <img
                src="/src/assets/SELMTECH.png"
                alt="Headphones"
                width="100"
                height="100"
                class="rounded-lg object-cover"
                style="aspect-ratio:100/100;object-fit:cover"
              />
            </div>
            <a class="flex items-center justify-between w-full" href="#">
              <span>Headphones</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="w-5 h-5"
              >
                <path d="m9 18 6-6-6-6"></path>
              </svg>
            </a>
          </div>
          <div class="bg-muted text-foreground rounded-lg p-6 flex flex-col items-start justify-between hover:bg-accent hover:text-accent-foreground transition-colors">
            <a class="flex items-center justify-between w-full" href="#">
              <span>Speakers</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="w-5 h-5"
              >
                <path d="m9 18 6-6-6-6"></path>
              </svg>
            </a>
          </div>
          <div class="bg-muted text-foreground rounded-lg p-6 flex flex-col items-start justify-between hover:bg-accent hover:text-accent-foreground transition-colors">
            <div class="flex items-center gap-4 mb-4">
              <img
                src="/src/assets/SELMTECH.png"
                alt="Earbuds"
                width="100"
                height="100"
                class="rounded-lg object-cover"
                style="aspect-ratio:100/100;object-fit:cover"
              />
              <h3 class="text-lg font-semibold">Earbuds</h3>
            </div>
            <a class="flex items-center justify-between w-full" href="#">
              <span>Earbuds</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="w-5 h-5"
              >
                <path d="m9 18 6-6-6-6"></path>
              </svg>
            </a>
          </div>
          <div class="bg-muted text-foreground rounded-lg p-6 flex flex-col items-start justify-between hover:bg-accent hover:text-accent-foreground transition-colors">
            <div class="flex items-center gap-4 mb-4">
              <img
                src="/src/assets/SELMTECH.png"
                alt="Accessories"
                width="100"
                height="100"
                class="rounded-lg"
                style="aspect-ratio:100/100;object-fit:cover"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</div>  
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