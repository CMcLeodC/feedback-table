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
              v-for="topic in topics"
              :key="topic"
              :text="topic"
              :value="topic"
            ></v-chip>
          </v-chip-group>
        </v-responsive>
      </div>
    </v-sheet>
  </template>

<script setup>
const topics = [
        '📚 Tale',
        '💡 Quiz',
        '🎮 Game',
        '🎥 Video',
        '🎵 Audiobook',
        '🎓 Theory',
        '📰 PDF',
      ]
</script>

<style scoped></style>