<template>
    <v-data-table
    v-model:page="currentPage"
    :headers="fields"
    :items="feedbackList"
    :sort-by="[{ key: sortBy, order: sortDesc ? 'desc' : 'asc'}]"
    item-value="id"
    :items-per-page="perPage"
  >
  <template v-slot:bottom>
      <div class="text-center pt-2">
        <v-pagination
          v-model="currentPage"
          :length="pageCount"
        ></v-pagination>
      </div>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-btn
          text="More Info"
          class="text-none"
          size="small"
          variant="flat"
          flat
          @click="store.openModalWithID(item.id)"
          
        ></v-btn>
    </template>
</v-data-table>
  {{ console.log("currentPage from vuetify table component: ", currentPage) }}
</template>

<script setup>
import { onMounted } from 'vue';
import { useStore } from '../store';
import { storeToRefs } from 'pinia';
const store = useStore()

const { fields, sortBy, feedbackList, sortDesc, filterValue, currentPage, perPage, pageCount, openModalWithID } = storeToRefs(store)

// onMounted(() => {
//   store.fetchFeedback();
// });


</script>

<style>
table th, td {
 color: black;
}
</style>