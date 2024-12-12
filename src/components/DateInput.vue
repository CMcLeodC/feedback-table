<template>
  <div class="d-flex justify-center">
    <v-container>
      <v-date-input v-model="mis_fechas" label="Select range" max-width="368" multiple="range"></v-date-input>

    </v-container>
  </div>
</template>

<script setup>
import { useStore } from '../store';
const store = useStore()
import { ref, computed } from 'vue';
const customFormatHeader = computed(() => {
  return mis_fechas.value && mis_fechas.value.length <= 1 ? "Select Dates" :
    `${new Date(mis_fechas.value[0]).toLocaleDateString()} - ${new Date(mis_fechas.value[mis_fechas.value.length - 1]).toLocaleDateString()}`
})
const mis_fechas = ref([]);
store.dates = mis_fechas;
</script>
<style scoped></style>