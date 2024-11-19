import { defineStore } from 'pinia'

// You can name the return value of `defineStore()` anything you want,
// but it's best to use the name of the store and surround it with `use`
// and `Store` (e.g. `useUserStore`, `useCartStore`, `useProductStore`)
// the first argument is a unique id of the store across your application
export const useAlertsStore = defineStore('alerts', {
  // other options...
})

export const useCounterStore = defineStore('counter', {
  state: () => ({ count: 0, name: 'Connor'}),
  getters: {
    doubleCount: (state) => state.count * 2,
  },
  actions: {
    increment() {
      this.count++
    },
  },
})

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
    perPage: 30

  }),
  actions: {
    fetchFeedback () {
      fetch(`/api/feedback?filter=${this.filterValue}&sort=${this.sortBy}&desc=${this.sortDesc}&page=${this.currentPage}&per_page=${this.perPage}`)
        .then((response) => response.json())
        .then((data) => {
          // totalRows.value = data.total
          this.feedbackList = data.data
          console.log("data.total is: ", data.total)
          console.log("Feedback list: ", this.feedbackList);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
  }
})