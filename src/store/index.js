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
    dreamerInfo: {},
    userInfo: {},
    contentArt: {},
    items: ['English', 'Spanish', 'French', 'Catalan'],
    value: ['Portuguese', 'Italian', 'Turkish', 'Latam'],
    types: ['Game', 'Tale', 'Quiz', 'Theory', 'Video', 'Audiobook', 'PDF'],
    typesOptions: ['Game', 'Tale', 'Quiz', 'Theory', 'Video', 'Audiobook', 'PDF'],
    completed: true
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
    countPages(dataTotal, perPage) {
      this.pageCount = Math.ceil(dataTotal / perPage)
    },
    async openModalWithID(id) {
      try {
        const response = await fetch('/api/feedback/' + id);
        const data = await response.json();
        this.moreInfo = data;
        console.log("this.moreInfo: ", this.moreInfo);
        console.log("This particular dreamer_id is: ", data.dreamer_id);
        await this.fetchDreamer(data.dreamer_id);
        await this.fetchUser(data.user_id);
        await this.fetchContentArt(data.content_id)
        this.showModal = true;
        console.log("completed: ", data.completed)
      } catch (error) {
        console.error('Error:', error);
      };
    },
    handleAvatarUrl(val) {
      return `http://localhost:5000/back/images/dreamer_avatars/AvatarSprite_${val}.png`
    },
    async fetchDreamer(id) {
      try {
        const response = await fetch('/api/dreamers/' + id)
        const data = await response.json()
        this.dreamerInfo = data;
      } catch (error) {
        console.error('Error:', error);
        this.dreamerInfo = null;
      };
    },
    async fetchUser(id) {
      try {
        const response = await fetch('/api/users/' + id)
        const data = await response.json()
        this.userInfo = data;
      } catch (error) {
        console.error('Error:', error);
        this.userInfo = null;
      };
    },
    async fetchContentArt(id) {
      try {
        const response = await fetch('/api/contents_arts/' + id);
        const data = await response.json();
        this.contentArt = data;
      } catch (error) {
        console.error('Error:', error);
        this.userInfo = null;
      };
    }
  }
})