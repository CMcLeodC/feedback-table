<template>
    <vuetable ref="vuetable"
      api-url="https://jsonplaceholder.typicode.com/todos"
      :fields="['userId', 'id', 'title', 'completed']"
      :sort-order="sortOrder"
      data-path=""
      pagination-path=""
    ></vuetable>
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