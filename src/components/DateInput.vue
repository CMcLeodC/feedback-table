<template>
  <div class="d-flex justify-center">
    <v-container>
      <v-date-input v-model="store.dates" label="Select range" max-width="368" multiple="range" clearable></v-date-input>
    </v-container>
  </div>
</template>

<script setup>
import { useStore } from '../store';
import { watch } from 'vue';

const store = useStore();

watch(
  () => store.dates,
  (newDates) => {
    if (newDates?.length > 0) {
      const formatDate = (date) => {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
      };
      store.startDate = formatDate(newDates[0]); 
      store.endDate = formatDate(newDates[newDates.length - 1]);
    } else {
      store.startDate = "";
      store.endDate = "";
    }
  },
  { immediate: true }
);
</script>
<style scoped></style>