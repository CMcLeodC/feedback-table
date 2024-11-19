<template>
    <div class="container">
        <div class="counter">
            {{ store.count }}
        </div>
        <div class="buttons">
            <button @click="store.increment">+</button>
        </div>
        <h4>{{ store.name }}</h4>
        <h4>Double count is {{ store.doubleCount }}</h4>
    </div>
</template>

<script setup>
import { useCounterStore } from '../store';
import { computed } from 'vue';
import { storeToRefs } from 'pinia';

const store = useCounterStore()

const { name, doubleCount } = storeToRefs(store)
const { increment } = store

</script>

<style>
.container {
    width: 100%;
}
div {
    margin-bottom: 10px;
}
.counter {
    font-size: 80px;
    width: 100px;
    justify-self: center;
}

.buttons {
    font-size: 40px;
    width: 100px;
    margin: 0px 10px;
    justify-self: center;
}

</style>