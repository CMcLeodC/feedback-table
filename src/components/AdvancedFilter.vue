<template>
    <v-select
      v-model="store.selectPlace"
      :hint="`${store.selectPlace.state}, ${store.selectPlace.abbr}`"
      :items="store.items"
      itemTitle="state"
      itemValue="abbr"
      label="store.selectPlace"
      persistent-hint
      return-object
      single-line
    ></v-select>
</template>

<script setup>
import { useStore } from '../store';
import { storeToRefs } from 'pinia';
import { ref } from 'vue';

const store = useStore();
</script>