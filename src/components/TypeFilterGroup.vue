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
          <v-chip-group class="mt-3" column filter multiple v-model="mappedSelectedTypes">
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
import { computed } from 'vue';
const store = useStore()

const typeMappings = {
  '📚 Tale': 'TALE',
  '💡 Quiz': 'QUIZZ',
  '🎮 Game': 'GAME',
  '🎥 Video': 'VIDEO',
  '🎵 Audiobook': 'AUDIOBOOK',
  '🎓 Theory': 'THEORY',
  '📰 PDF': 'PDF'
};

const mappedSelectedTypes = computed({
  get: () =>
    store.selectedTypes.map((type) =>
      Object.values(typeMappings).includes(type)
        ? Object.keys(typeMappings).find((key) => typeMappings[key] === type) // Map database-friendly back to chip-friendly
        : type
    ),
  set: (newTypes) => {
    store.selectedTypes = newTypes.map((type) =>
      Object.keys(typeMappings).includes(type)
        ? typeMappings[type] // Map chip-friendly to database-friendly
        : type
    );
  },
});
</script>

<style scoped></style>