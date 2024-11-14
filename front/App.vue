<template>
  <div class="app-container">
    <h1>Feedback</h1>
    <div class="input-field">
      <input type="search" v-model="filterValue" id="search-bar" placeholder="Search feedback..." @keyup.enter="fetchFeedback">
      {{ console.log(filterValue) }}
    </div>
    {{console.log(sortBy)}}
    <div class="feedback-table">
      <BContainer>
        <BRow>
          <BCol>
            <div class="overflow-auto">
              <b-pagination
            v-model="currentPage"
            :total-rows="totalRows"
            :per-page="perPage"
            aria-controls="my-table"
            align="center"
            @update:model-value="fetchFeedback"/>
            
            <p class="mt-3 text-center">Current Page: {{ currentPage }}</p>
            {{ sortBy }}
              <BTable
              id="my-table"
              :items="feedbackList"
              :fields="fields"
              striped hover 
              
              
              :sort-by="[{ key: sortBy, order: sortDesc }]"
              >
              <template #cell(#)="data">
                {{ data.index + 1 }}
              </template>
              <template #cell(dreamer_avatar)="data">
                <img 
                :src="handleAvatarUrl(data.item.dreamer_avatar)"
                alt="Dreamer Avatar" style="width: 50px; height: 50px;" />
              </template>
              <template #cell(actions)="data">
                <BButton v-b-modal.modal-center @click="openModalWithID(data.item.id)">More Info</BButton>
              </template>
              <template #cell(level_name)="data">
                {{ data.item.level_name.charAt(0).toUpperCase() + data.item.level_name.slice(1) }}
              </template>
              <template #cell(score)="data">
                {{ data.item.score }}/{{ data.item.total_score }}
              </template>
            </BTable>
            <b-pagination
            v-model="currentPage"
            :total-rows="totalRows"
            :per-page="perPage"
            aria-controls="my-table"
            align="center"
            @update:model-value="fetchFeedback"/>

            <p class="mt-3 text-center">Current Page: {{ currentPage }}</p>
            </div>
          </BCol>
        </BRow>
      </BContainer>
    </div>

    <TableFeedback :feedbackList="feedbackList" :sortBy="sortBy" :sortDesc="sortDesc"/>

    <MoreInfoModal :moreInfo="moreInfo"/>
  </div>
  {{console.log(sortBy)}}
</template>

<script setup>
import { onMounted, ref, watch, computed } from 'vue'
import { BCol, BContainer, BRow, BTable } from 'bootstrap-vue-next'
import MoreInfoModal from './components/MoreInfoModal.vue';
import TableFeedback from './components/TableFeedback.vue';

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

    const fields = [
      { key: '#', label: '', sortable: false },
      { key: 'created_at', label: 'Date', sortable: true },
      { key: 'dreamer_avatar', label: '', sortable: false },
      { key: 'dreamer_name', label: 'Dreamer', sortable: true },
      { key: 'user_name', label: 'User', sortable: true },
      { key: 'content_title', label: 'Content', sortable: true },
      { key: 'level_name', label: 'Difficulty Level', sortable: true },
      { key: 'duration', label: 'Time (Seconds)', sortable: true },
      { key: 'score', label: 'Score', sortable: true },
      { key: 'actions', label: '', sortable: false },
    ];

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