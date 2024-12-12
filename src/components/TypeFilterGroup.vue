<template>
    <v-sheet
      class="mx-auto"
      max-width="400"
      rounded="xl"
      border
    >
      <div class="pa-4">
        <div class="text-h6">Select the type</div>
  
        <v-responsive class="overflow-y-auto" max-height="280">
          <v-chip-group class="mt-3" column filter multiple>
            <v-chip
              v-for="type in store.types"
              :key="type"
              :text="type"
              :value="type"
            ></v-chip>
          </v-chip-group>
        </v-responsive>
      </div>
    </v-sheet>
  </template>

<script setup>
import { useStore } from '../store';
const store = useStore()
</script>

<style scoped></style>