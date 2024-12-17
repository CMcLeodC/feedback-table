<template>
  <v-card>
    <v-container fluid>
      <v-row align="center">
        <v-col cols="12" sm="6">
          <LanguageFilterGroup />
        </v-col>
        <v-col cols="12" sm="6">
          <TypeFilterGroup />
        </v-col>
        <v-col
        class="d-flex"
        cols="12"
        sm="6"
      >
        <v-select
          :items="items"
          filled
          label="Completed"
          v-model="selectedCompleted"
        ></v-select>
      </v-col>
        <v-col cols="12" sm="6">
          <DateInput />
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script setup>
import { useStore } from '../store';
import { storeToRefs } from 'pinia';
import { ref, watch } from 'vue';
import TypeFilterGroup from './TypeFilterGroup.vue';
import LanguageFilterGroup from './LanguageFilterGroup.vue';
import DateInput from './DateInput.vue';

const store = useStore();

const items = ['Show All', 'Completed', 'Not Completed']
const selectedCompleted = ref("")
watch(selectedCompleted, newValue => {
  if (newValue === 'Completed') {
    store.completed = true
  } else if (newValue === 'Not Completed') {
    store.completed = false
  } else {
    store.completed = null
  }
})


</script>