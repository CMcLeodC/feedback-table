<template>
    <div class="d-flex justify-center">
        <v-container>
            <v-date-input
              v-model="model"
              label="Select range"
              max-width="368"
              multiple="range"
            ></v-date-input>

        </v-container>
    </div>
  </template>

<script setup>
import { ref, computed } from 'vue';
const model = null;

</script>

<style scoped>

</style>