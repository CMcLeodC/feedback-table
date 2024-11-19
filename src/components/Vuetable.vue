<template>
    <vuetable ref="vuetable"
      api-url="https://jsonplaceholder.typicode.com/todos"
      :fields="['userId', 'id', 'title', 'completed']"
      :sort-order="sortOrder"
      data-path=""
      pagination-path=""
    ></vuetable>
    <!-- <div v-if="feedbackList.length">
      <h2>Feedback Data:</h2>
      <ul>
        <li v-for="feedback in feedbackList" :key="feedback.id">
          <strong>ID:</strong> {{ feedback.id }}<br />
          <strong>Date:</strong> {{ feedback.created_at }}<br />
          <strong>Dreamer:</strong> {{ feedback.dreamer_name }}<br />
          <strong>User:</strong> {{ feedback.user_name }}<br />
          <strong>Content:</strong> {{ feedback.content_identifier }}<br />
          <strong>Difficulty Level:</strong> {{ feedback.level_name.charAt(0).toUpperCase() + feedback.level_name.slice(1) }}<br />
          <strong>Time (Duration):</strong> {{ feedback.duration }}<br />
          <strong>Total Score:</strong> {{ feedback.total_score }}<br />
          <hr />
        </li>
      </ul>
    </div>
    <p v-else>No feedback data available</p> -->

    
  </template>
  
  <script>
  import Vuetable from 'vuetable-2'
  
  export default {
    components: {
      Vuetable
    },

    // fields: [
    //   { key: '#', label: '#', sortable: false },
    //   { key: 'created_at', label: 'Date', sortable: true },
    //   { key: 'dreamer_avatar', label: 'DAP', sortable: false },
    //   { key: 'dreamer_name', label: 'Dreamer', sortable: true },
    //   { key: 'user_name', label: 'User', sortable: true },
    //   { key: 'content_title', label: 'Content', sortable: true },
    //   { key: 'level_name', label: 'Difficulty Level', sortable: true },
    //   { key: 'duration', label: 'Time (Duration)', sortable: true },
    //   { key: 'total_score', label: 'Total Score', sortable: true },
    //   { key: 'actions', label: '', sortable: false },
    // ]
  }
  </script>

  

# if sort_field == 'dateDesc':
#     query = query.order_by(Feedback.created_at.desc())
# elif sort_field == 'dateAsc':
#     query = query.order_by(Feedback.duration.asc())
# elif sort_field == 'duration':
#     query = query.order_by(Feedback.duration.desc())
# elif sort_field == 'score':
#     query = query.order_by(Feedback.total_score.desc()) 