<template>
    <v-data-table
    :headers="store.fields"
    :items="store.feedbackList"
    :sort-by="[{ key: store.sortBy, order: 'desc' }]"
  ></v-data-table>

</template>

<script setup>
import { onMounted } from 'vue';
import { useStore } from '../store';
import { storeToRefs } from 'pinia';
const store = useStore()

const { fields, sortBy, feedbackList, sortDesc, filterValue, currentPage, perPage } = storeToRefs(store)

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