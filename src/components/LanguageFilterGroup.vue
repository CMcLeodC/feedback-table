<template>
    <v-sheet
      class="mx-auto"
      max-width="400"
      rounded="xl"
      border
    >
      <div class="pa-4">
        <div class="text-h6">Select the language</div>
  
        <v-responsive class="overflow-y-auto" max-height="280">
          <v-chip-group class="mt-3" column filter multiple>
            <v-chip
              v-for="language in store.languages"
              :key="language"
              :text="language"
              :value="language"
            ></v-chip>
          </v-chip-group>
        </v-responsive>
      </div>
    </v-sheet>
  </template>

<script setup>
import { useStore } from '../store';

import { storeToRefs } from 'pinia';
const store = useStore()
</script>

<style scoped></style>