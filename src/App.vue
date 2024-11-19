<template>
  <div class="app-container">
    <h1>Feedback</h1>
    <VuetifyTable />
    <div class="input-field">
      <input type="search" v-model="filterValue" id="search-bar" placeholder="Search feedback..."
        @keyup.enter="fetchFeedback">
      {{ console.log(filterValue) }}
    </div>
    {{console.log(sortBy)}}
    <!-- <div class="feedback-table">
      <Bootstraptable 
        :feedbackList="feedbackList" 
        :fields="store.fields"
        :sortBy="sortBy"
        :sortDesc="sortDesc"
        :currentPage="currentPage"
        :perPage="perPage"
        :totalRows="totalRows"
        :handleAvatarUrl="handleAvatarUrl"
        />
    </div> -->

    <TableFeedback :feedbackList="feedbackList" :fields="store.fields" :sortBy="sortBy" :sortDesc="sortDesc" />

    <MoreInfoModal :moreInfo="moreInfo" />
  </div>
  {{console.log(sortBy)}}
</template>

<script setup>
import { onMounted, ref, watch, computed } from 'vue'
import MoreInfoModal from './components/MoreInfoModal.vue';
import TableFeedback from './components/TableFeedback.vue';
// import Bootstraptable from './components/Bootstraptable.vue';
import { useStore } from './store';
import { storeToRefs } from 'pinia';
import VuetifyTable from './components/VuetifyTable.vue';

const store = useStore()

const { fields } = storeToRefs(store)

const isModalOpen = ref(false);
const filterValue = ref("");
const feedbackList = ref([]);
const moreInfo = ref({});
const sortBy = ref("user_name");
const sortDesc = ref(false);
const selectedID = ref(null);
const perPage = ref(30);
const currentPage = ref(1);
const totalRows = ref(null)



const rows = computed(() => feedbackList.value.length)

const handleAvatarUrl = (val) => {
  return `http://localhost:5000/back/images/dreamer_avatars/AvatarSprite_${val}.png`
}
const openModalWithID = (id) => {
  selectedID.value = id
  fetch('/api/feedback/' + id)
    .then((response) => response.json())
    .then((data) => {
      moreInfo.value = data;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

const fetchFeedback = () => {
  fetch(`/api/feedback?filter=${filterValue.value}&sort=${sortBy.value}&desc=${sortDesc.value}&page=${currentPage.value}&per_page=${perPage.value}`)
    .then((response) => response.json())
    .then((data) => {
      totalRows.value = data.total
      feedbackList.value = data.data
      console.log("data.total is: ", data.total)
      console.log("Feedback list: ", feedbackList.value);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

onMounted(() => {
  fetchFeedback();
});

</script>

<style>
h1 {
  color: #FFFFFF;
}

.app-container {
  font-family: sans-serif;
  font-size: 14px;
  background-color: #1E1E2F;
  color: #FFFFFF;
}

.input-field {
  display: flex;
  justify-content: center;
  margin: 15px;
}

#search-bar {
  width: 50%;
  padding: 8px;
  border-radius: 5px;
  border: 1px solid white;
  background-color: #333344;
  color: white;
  text-align: center;
  font-size: 18px;
}

.feedback-table .table-striped tbody tr:nth-of-type(odd) {
  background-color: #2A2A3B;
  color: #FFFFFF;
  font-weight: bold;
}

.feedback-table .table-striped tbody tr:nth-of-type(even) {
  background-color: #1E1E2F;
  color: #FFFFFF;
  font-weight: bold;
}

.feedback-table .table-striped tbody tr:nth-of-type(odd) button {
  background-color: #FF6B6B;
  border: none;
  border-radius: 10%;
  color: #FFFFFF;
}

.feedback-table .table-striped tbody tr:nth-of-type(even) button {
  background-color: #4CAF50;
  border: none;
  border-radius: 10%;
  color: #FFFFFF;
}

.feedback-table .table-striped th,
.feedback-table .table-striped td {
  color: #FFFFFF;
}

.feedback-table th {
  background-color: #333344;
  color: #FFFFFF !important;
  white-space: nowrap;
  padding-right: 20px;
}

.feedback-table th .bv-sortable-handle {
  display: inline-flex;
  align-items: center;
}

.feedback-table th .bv-sortable-handle svg {
  margin-left: 5px;
}
</style>