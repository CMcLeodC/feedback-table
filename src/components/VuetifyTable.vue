<template>
    <v-data-table
    :headers="store.fields"
    :items="store.feedbackList"
    :sort-by="[{ key: store.sortBy, order: 'desc' }, { key: 'duration', order: 'desc' }]"
    multi-sort
  ></v-data-table>
  {{ console.log("console logged store.fields: ", store.fields) }}
  {{ console.log("console logged store.feedbacklist: ", store.feedbackList) }}
</template>

<script setup>
import { onMounted } from 'vue';
import { useStore } from '../store';
import { storeToRefs } from 'pinia';
const store = useStore()

const { fields, sortBy, feedbackList } = storeToRefs(store)

const data = () => {
      return {
        // headers: store.fields,
        
      }
    }

onMounted(() => {
  store.fetchFeedback();
});
</script>

<style>
table th, td {
 color: black;
}
</style>