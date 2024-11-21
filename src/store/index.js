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
    currentPage: 2,
    perPage: 30,
    dataTotal: 30,
    pageCount: 3
    
  }),
  actions: {
    fetchFeedback () {
      fetch(`/api/feedback?filter=${this.filterValue}&sort=${this.sortBy}&desc=${this.sortDesc}&page=${this.currentPage}&per_page=${this.perPage}`)
        .then((response) => response.json())
        .then((data) => {
          // totalRows.value = data.total
          this.feedbackList = data.data
          this.dataTotal = data.total
          console.log("data.total is: ", data.total)
          console.log("Feedback list from fetchFeedback: ", this.feedbackList);
          this.countPages(this.dataTotal, this.perPage);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    sortTable (columnTitle) {
      if (this.sortBy === columnTitle) {
        this.sortDesc = !this.sortDesc;
        console.log("If yes ColumnTitle: ", columnTitle);
      } else {
        this.sortBy = columnTitle;
        this.sortDesc = false;
        console.log("Else ColumnTitle: ", columnTitle);
      }
      
      console.log("sortTable working");
      
      this.fetchFeedback();
    },
    countPages (dataTotal, perPage) {
      this.pageCount = Math.ceil(dataTotal/perPage)
    }
   }
})