<template>
    <v-container>
      <v-row justify="space-around">
        {{ mis_fechas }}
        <v-date-picker v-model="mis_fechas" show-adjacent-months multiple="range">
            <template #header>
                {{ customFormatHeader }}
            </template>
        </v-date-picker>
      </v-row>
    </v-container>
  </template>

<script setup>
import { ref, computed } from 'vue';
    const customFormatHeader = computed(() => {
        return mis_fechas.value && mis_fechas.value.length <= 1 ? "Select Dates" : 
        `${new Date(mis_fechas.value[0]).toLocaleDateString()} - ${new Date(mis_fechas.value[mis_fechas.value.length-1]).toLocaleDateString()}`
    })
    const mis_fechas = ref([])
</script>

<style scoped>

</style>