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
    showModal: false,
    dreamerInfo: [],
    cards: [
      { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 4 },
      { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 4 },
      { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 4 },
    ]
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
      fetch('/api/feedback/' + id)
        .then((response) => response.json())
        .then((data) => {
          this.moreInfo = data;
          console.log("this.moreInfo: ", this.moreInfo);
          this.showModal = true;
          console.log("This particular dreamer_id is: ", data.dreamer_id);          
          this.fetchDreamer(data.dreamer_id);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    handleAvatarUrl (val) {
      return `http://localhost:5000/back/images/dreamer_avatars/AvatarSprite_${val}.png`
    },
    fetchDreamer (id) {
      fetch('/api/dreamers/' + id)
      .then((response) => response.json())
      .then((data) =>{
        this.dreamerInfo = data;
        console.log("This is the dreamer Info: ", data);        
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    }
    
   }
})