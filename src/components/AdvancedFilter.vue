<template>
    <v-card>
    <v-container fluid>
      <v-row
        align="center"
      >
        <v-col
          cols="12"
          sm="6"
        >
          <v-select
            v-model="store.value"
            :items="store.items"
            attach
            chips
            label="Languages"
            multiple
          ></v-select>
        </v-col>
        <v-col
          cols="12"
          sm="6"
        >
          <v-select
            v-model="store.types"
            :items="store.types"
            filled
            chips
            label="Type"
            multiple
          ></v-select>
        </v-col>
        <v-col
          cols="12"
          sm="6"
        >
          <v-select
            v-model="store.value"
            :items="store.items"
            chips
            label="Completed"
            multiple
            outlined
          ></v-select>
        </v-col>
        <v-col
          cols="12"
          sm="6"
        >
          <v-select
            v-model="store.value"
            :items="store.items"
            chips
            label="Dates"
            multiple
            solo
          ></v-select>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script setup>
import { useStore } from '../store';
import { storeToRefs } from 'pinia';
import { ref } from 'vue';

const store = useStore();
</script>