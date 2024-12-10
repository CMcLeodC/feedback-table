<template>
  <v-card>
    <v-container fluid>
      <v-row align="center">
        <v-col cols="12" sm="6">
          <!-- <v-select
            v-model="store.value"
            :items="store.items"
            attach
            chips
            label="Languages"
            multiple
          ></v-select> -->
          <LanguageFilterGroup />
        </v-col>
        <v-col cols="12" sm="6">
          <!-- <v-select
            v-model="store.types"
            :items="store.typesOptions"
            filled
            chips
            label="Type"
            multiple
            clearable
          >
        </v-select> -->
          <TypeFilterGroup />
        </v-col>
        <v-col cols="12" sm="6">
          <!-- <v-select
            v-model="store.value"
            :items="store.items"
            chips
            label="Completed"
            multiple
            outlined
          ></v-select> -->
          <v-chip :model-value="true" class="ms-16" color="teal" prepend-icon="mdi-checkbox-marked-circle" closable>
            Completed
          </v-chip>
        </v-col>
        <v-col cols="12" sm="6">
          <!-- <v-select
            v-model="store.value"
            :items="store.items"
            chips
            label="Dates"
            multiple
            solo
          ></v-select> -->
          <DateInput />
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script setup>
import { useStore } from '../store';
import { storeToRefs } from 'pinia';
import { ref } from 'vue';
import TypeFilterGroup from './TypeFilterGroup.vue';
import LanguageFilterGroup from './LanguageFilterGroup.vue';
import DateInput from './DateInput.vue';

const store = useStore();
</script>