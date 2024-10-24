<template>
  <div class="app-container">
    <h1>Feedback</h1>

    <h1>Modal!!!</h1>
    <Teleport to="#modal">
      <div class="modal-bg" v-if="isModalOpen" @click.self="isModalOpen = false">
        <div class="modal">
          <!-- <p>dreamer avatar: {{ moreInfo.dreamer_avatar }}</p>
          <p>description: {{ moreInfo.content_title }}</p>
          <p>language: {{ moreInfo.lang_id }}</p>
          <p>Click outside the modal to close it</p> -->
          <p>this is the modal</p>
          {{ console.log('Modal is rendering') }}
        </div>
      </div>
    </Teleport>


    <!-- <button @click="fetchFeedback">Fetch Feedback Data</button> -->
    <p>* the DAP in the table stands for Dreamer Avatar pic *</p>

    <div class="input-field">
      <input v-model="filterValue" placeholder="Type to filter..." @input="applyFilter" />
    </div>
    <div class="feedback-table">
      <!-- <div class="sort-options">
        <select v-model="sortBy" @change="fetchFeedback">
          <option value="user_name">User</option>
          <option value="created_at">Date</option>
          <option value="duration">Duration</option>
          <option value="total_score">Score</option>
        </select>
        <select v-model="sortDesc" @change="fetchFeedback">
          <option :value="true">Descending</option>
          <option :value="false">Ascending</option>
        </select>
      </div> -->
      {{ sortDesc }} - {{ sortBy }}
      <b-table 
        :items="feedbackList" 
        :fields="fields" 
        striped
        hover
        :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc"
        >
        <!-- <template #cell(#)="data">
          {{ data.index + 1 }}
        </template>
        <template #cell(actions)="data">
          <button class="btn btn-primary" @click="toggleModal(data.item.id)">
            More Info
          </button>
        </template> -->
      </b-table>
    </div>
    <div v-if="feedbackList.length">
      <h2>Feedback Data:</h2>
      <ul>
        <li v-for="feedback in feedbackList" :key="feedback.id">
          <strong>ID:</strong> {{ feedback.id }}<br />
          <strong>Date:</strong> {{ feedback.created_at }}<br />
          <strong>Dreamer:</strong> {{ feedback.dreamer_name }}<br />
          <strong>User:</strong> {{ feedback.user_name }}<br />
          <strong>Content:</strong> {{ feedback.content_identifier }}<br />
          <strong>Difficulty Level:</strong> {{ feedback.level_name }}<br />
          <strong>Time (Duration):</strong> {{ feedback.duration }}<br />
          <strong>Total Score:</strong> {{ feedback.total_score }}<br />
          <hr />
        </li>
      </ul>
    </div>
    <p v-else>No feedback data available</p>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue'

export default {
  setup() {
    const isModalOpen = ref(false);
    const filterValue = ref("");
    const feedbackList = ref([]);
    const moreInfo = ref({});
    const sortBy = ref("user_name");
    const sortDesc = ref(false);

    const toggleModal = (id) => {
      isModalOpen.value = !isModalOpen.value;
      if (isModalOpen.value) {
        openMoreInfoModal(id);
      }
      console.log('Modal data:', moreInfo.value);

    };

    const fields = [
      { key: '#', label: '#', sortable: false },
      { key: 'created_at', label: 'Date', sortable: true },
      { key: 'dreamer_avatar', label: 'DAP', sortable: false },
      { key: 'dreamer_name', label: 'Dreamer', sortable: true },
      { key: 'user_name', label: 'User', sortable: true },
      { key: 'content_title', label: 'Content', sortable: true },
      { key: 'level_name', label: 'Difficulty Level', sortable: true },
      { key: 'duration', label: 'Time (Duration)', sortable: true },
      { key: 'total_score', label: 'Total Score', sortable: true },
      { key: 'actions', label: '', sortable: false },
    ];

    const openMoreInfoModal = (id) => {
      fetch('/api/feedback/' + id)
        .then((response) => response.json())
        .then((data) => {
          console.log('Fetched data for modal:', data);

          moreInfo.value = data;
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }

    const fetchFeedback = () => {
      fetch(`/api/feedback?filter=${filterValue.value}&sort=${sortBy.value}&desc=${sortDesc.value}`)
        .then((response) => response.json())
        .then((data) => {
          feedbackList.value = data;
          console.log(data);
          
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    };

    // const onSortChanged = () => {
    //   const { sortBy, sortDesc: desc } = context;
    //   const sortKey = desc ? `${field}Desc` : `${field}Asc`;
    //   sortBy.value = sortKey;
    //   sortDesc.value = desc;
    //   fetchFeedback();
    // };


    const applyFilter = () => {
      fetchFeedback();
    };

    onMounted(() => {
      fetchFeedback();
    });

    return {
      isModalOpen,
      filterValue,
      feedbackList,
      moreInfo,
      sortBy,
      fetchFeedback,
      applyFilter,
      toggleModal,
      fields,
      // onSortChanged,
      sortDesc
    };
  },
};
</script>

<style>
h1 {
  color: #FFFFFF; /* White text for headings */
}

.app-container {
  font-family: sans-serif;
  font-size: 14px;
  background-color: #1E1E2F; /* Dark background for the app */
  color: #FFFFFF; /* White text */
}

.input-field {
  margin: 15px;
}

/* Feedback table styles */
.feedback-table .table-striped tbody tr:nth-of-type(odd) {
  background-color: #2A2A3B; /* Dark grey for odd rows */
  color: #FFFFFF; /* White text for readability */
  font-weight: bold;
}

.feedback-table .table-striped tbody tr:nth-of-type(even) {
  background-color: #1E1E2F; /* Even darker grey for even rows */
  color: #FFFFFF; /* White text for readability */
  font-weight: bold;
}

/* Bright and contrasting buttons */
.feedback-table .table-striped tbody tr:nth-of-type(odd) button {
  background-color: #FF6B6B; /* Bright red for buttons on odd rows */
  border: none;
  border-radius: 10%;
  color: #FFFFFF; /* White text */
}

.feedback-table .table-striped tbody tr:nth-of-type(even) button {
  background-color: #4CAF50; /* Bright green for buttons on even rows */
  border: none;
  border-radius: 10%;
  color: #FFFFFF; /* White text */
}

/* Header styles */
.feedback-table .table-striped th,
.feedback-table .table-striped td {
  color: #FFFFFF; /* White text for table headers */
}

.feedback-table th {
  background-color: #333344; /* Darker grey background for headers */
  color: #FFFFFF !important; /* White text for headers */
}

.modal-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.7); /* Dark overlay background */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  visibility: visible;
  opacity: 1;
}

.modal {
  background: #333344; /* Dark grey for modal background */
  padding: 20px;
  max-width: 600px;
  max-height: 600px;
  border-radius: 8px;
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5); /* Softer shadow */
  z-index: 10000;
  display: block;
  opacity: 1;
  visibility: visible;
  position: relative;
  overflow: auto;
}

.modal-content {
  color: #000000;
}

.b-table-sort-icon {
  display: inline-block;
  margin-left: 5px;
  color: #FFFFFF; /* White sort icon */
}

.sorted-asc .b-table-sort-icon::after {
  content: "▲"; /* Up arrow for ascending */
  font-size: 12px;
}

.sorted-desc .b-table-sort-icon::after {
  content: "▼"; /* Down arrow for descending */
  font-size: 12px;
}


</style>