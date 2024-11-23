import { defineStore } from 'pinia'

export const useStore = defineStore('storeID', {
  state: () => ({
    fields: ([
      { key: '#', title: '', sortable: false },
      { key: 'created_at', title: 'Date', sortable: true },
      { key: 'dreamer_avatar', title: '', sortable: false },
      { key: 'dreamer_name', title: 'Dreamer', sortable: true },
      { key: 'user_name', title: 'User', sortable: true },
      { key: 'content_title', title: 'Content', sortable: true },
      { key: 'level_name', title: 'Difficulty Level', sortable: true },
      { key: 'duration', title: 'Time (Seconds)', sortable: true },
      { key: 'score', title: 'Score', sortable: true },
      { key: 'actions', title: '', sortable: false },
    ]),
    feedbackList: [],
    sortBy: "user_name",
    filterValue: "",
    sortDesc: false,
    currentPage: 1,
    perPage: 30,
    dataTotal: 30,
    pageCount: 3,
    moreInfo: ({}),
    // selectedID: (null)
  }),
  actions: {
    async fetchFeedback() {
      try {
          const response = await fetch(`/api/feedback?filter=${this.filterValue}&sort=${this.sortBy}&desc=${this.sortDesc}&page=${this.currentPage}&per_page=${this.perPage}`);
          const data = await response.json();
          this.feedbackList = data.data;
          this.totalItems = data.total; 
          this.pageCount = Math.ceil(this.totalItems / this.perPage);
          console.log(this.feedbackList);
      } catch (error) {
          console.error("Error fetching feedback:", error);
          
          
      }
    },
    countPages (dataTotal, perPage) {
      this.pageCount = Math.ceil(dataTotal/perPage)
    },
    openModalWithID (id) {
      // selectedID.value = id
      fetch('/api/feedback/' + id)
        .then((response) => response.json())
        .then((data) => {
          this.moreInfo = data;
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }
    
   }
})