<template>
  <div v-if="store.showModal" class="modal-overlay" @click="closeModal"></div>

  <v-card v-if="store.showModal" class="vuetify-modal-container mx-auto" max-width="1700">
    <v-container fluid>
      <v-row dense justify="space-between">
        <!-- Card 1 -->
        <v-col cols="12" md="4">
          <v-card class="player-card mx-auto" max-width="344">
            <template v-slot:title>
              <h1 class="modal-header">Player</h1>
            </template>
            <v-card-text>
              <v-avatar size="100" class="mx-auto mb-4">
                <v-img :src="store.handleAvatarUrl(store.dreamerInfo.avatar)" alt="Player Avatar" />
              </v-avatar>
              <div class="text-center text-h5 font-weight-bold">
                {{ store.dreamerInfo.name }}
                <div class="flag-container">
                  <v-img :src="`/assets/flag${store.moreInfo.lang_id}.png`" class="flag-image" alt="Language Flag" />
                </div>
              </div>

              <div class="mt-3">
                <div>Birthdate: {{ new Date(store.dreamerInfo.birthdate).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' }) }}</div>
                <div>Age: {{ store.dreamerInfo.age }}</div>
              </div>
              <div class="mt-3 d-flex justify-space-between">
                <div>Coins: {{ store.dreamerInfo.coins }}</div>
                <div>Gems: {{ store.dreamerInfo.gems }}</div>
              </div>
              <div class="mt-3">
                <div class="user-info-box">
                  <div class="user-info-header">
                    <span>User Info</span>
                  </div>
                  <div class="user-info-content">
                    <div>{{ store.userInfo.name }}</div>
                    <div>{{ store.userInfo.email }}</div>
                  </div>
                </div>
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn color="deep-purple-accent-4" text="Learn More" variant="text"></v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        {{ console.log("hello", store.dreamerInfo.name) }}
        <!-- Card 2 -->

        <v-col cols="12" md="4">
          <v-card class="counter-card mx-auto" max-width="344">
            <template v-slot:title>
              <h1 class="modal-header">Counter</h1>
            </template>
            <v-card-text>
              <v-img class="thumbnail-art" height="200" :src="store.contentArt.thumbnail_url" cover></v-img>
              <div class="text-center text-h5 font-weight-bold">
                {{ store.moreInfo.content_title }}
              </div>
              <div class="mt-3">
                <div>
                  {{  store.moreInfo.content_description }}
                </div>
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn color="deep-purple-accent-4" text="Learn More" variant="text"></v-btn>
            </v-card-actions>
          </v-card>
        </v-col>

        <!-- Card 3 -->
        <v-col cols="12" md="4">
          <v-card class="game-card mx-auto" max-width="344">
            <template v-slot:title>
              <h1 class="modal-header">Game</h1>
            </template>
            <v-card-text>
              <div class="d-flex align-items-center mb-3">
                <div class="flag-container">
                  <v-img :src="`/assets/flag${store.moreInfo.lang_id}.png`" class="flag-image" alt="Language Flag" />
                </div>
                <span class="text-h5">{{ store.moreInfo.lang_local_name }}</span>
              </div>

              <!-- Completed Status -->
              <template>
                <div class="d-flex align-items-center mb-3">
                  <div v-if="store.moreInfo.completed" class="tick-container me-2">
                    <img 
                      src="/assets/check-tick-mark-in-green-circle.jpg" 
                      alt="Success Tick" 
                      class="tick-icon"
                    />
                  </div>
                  <span class="text-h6">Completed</span>
                </div>
              </template>


              <!-- Time and Score -->
              <div class="mt-3">
                <div>Time: {{ store.moreInfo.duration }}</div>
                <div>Score: {{ store.moreInfo.score }} / {{ store.moreInfo.total_score }}</div>
                <div>Cat: {{ store.moreInfo.category_name }}</div>
                <div>Sub-Cat: {{ store.moreInfo.subcategory_name }}</div>
                <div>Type: {{ store.moreInfo.type_name }}</div>
                <div>Details: {{ store.moreInfo.details }}</div>
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn color="deep-purple-accent-4" text="More Info" variant="text"></v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>


<script setup>
import { useStore } from '../store';
import { storeToRefs } from 'pinia';
import { ref } from 'vue';

const store = useStore();
const { cards, dreamerInfo, userInfo, contentArt } = storeToRefs(store);
// const showModal = ref(false);
console.log(contentArt);

const closeModal = () => {
  store.showModal = false;
};

const openModal = () => {
  store.showModal = true;
};

</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.vuetify-modal-container {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
  padding: 20px;
  background-color: #2A2A3B !important;
  color: #FFFFFF;
  max-height: 80vh; 
  overflow-y: auto;
}

.vuetify-modal-container.v-card {
  background-color: #2A2A3B !important; 
  position: fixed !important;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.modal-header {
  color: #FFD700; /* Golden color for better contrast */
  font-size: 24px; /* Bigger font size */
  font-weight: bold; /* Emphasize header weight */
  text-align: center; /* Center alignment for importance */
  margin-bottom: 20px; /* Space below header */
  text-transform: uppercase; /* Make text uppercase for a header-like feel */
  border-bottom: 2px solid #FFD700; /* Divider below the header */
  padding-bottom: 10px; /* Spacing to separate text from border */
}

h1 {
  color: #FFFFFF;
}

.app-container {
  font-family: sans-serif;
  font-size: 14px;
  background-color: #1E1E2F;
  color: #FFFFFF;
}

.v-card.player-card, 
.v-card.counter-card, 
.v-card.game-card {
  background-color: #2A2A3B !important; 
  color: #FFFFFF !important;
  border: 2px solid #3A3A4D;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  padding: 20px;
}

.v-card {
  background-color: #2A2A3B !important; 
  color: #FFFFFF !important;
  box-shadow: none !important;
  border-radius: 10px; 
  border: 1px solid #3A3A4D;
}

.v-col .v-card.player-card {
  background-color: #2A2A3B; /* Matches table's odd rows */
}

.v-col .v-card.counter-card {
  background-color: #1E1E2F; /* Matches table's even rows */
}

.v-col .v-card.game-card {
  background-color: #2E2E44; /* Slightly lighter for better contrast */
  border: 2px solid #4B4B63;
  border-radius: 10px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
  padding: 20px;
}

.v-col .v-card.game-card .v-card-title {
  color: #FFFFFF;
  font-weight: bold;
  font-size: 22px;
  text-align: center;
  margin-bottom: 15px;
}

.v-col .v-card.game-card .v-card-text div {
  color: #B0B0C3;
  font-size: 16px;
  margin-bottom: 10px;
}

.v-col .v-card.game-card .v-btn {
  background-color: #6A6AFF;
  color: #FFFFFF;
  font-weight: bold;
  border-radius: 8px;
}

.v-col .v-card.game-card .v-btn:hover {
  background-color: #8080FF;
}


.v-card-title, .v-card-text {
  color: #CCCCCC !important;
}

.v-card-title {
  font-size: 28px !important;
  font-weight: bold;
  text-align: center;
  margin-bottom: 20px;
  color: #FFFFFF;
}

.v-card-text div {
  margin-bottom: 10px;
  color: #CCCCCC;
}

.v-btn {
  background-color: #333344;
  color: #FFFFFF;
  border: none;
}

.v-btn:hover {
  background-color: #444455;
  transition: background-color 0.2s ease;
}

.v-icon {
  vertical-align: middle;
}

.thumbnail-art {
  margin-top: -10px;
  margin-bottom: -30px;
}

.v-avatar {
  display: flex !important;
  justify-content: center !important;
  margin: 0 auto !important;
  align-items: center !important;
  border: 2px solid white !important;
}

.v-col {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.flag-container {
  width: 60px;
  height: 40px;
  display: inline-block;
  overflow: hidden;
  border-radius: 4px;
}

.flag-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}

.tick-container {
  display: flex;
  align-items: center; /* Center image vertically */
  justify-content: center; /* Center image horizontally */
}

.tick-icon {
  width: 32px; /* Set width */
  height: 32px; /* Set height */
  object-fit: contain; /* Ensure the image scales without distortion */
}

.user-info-box {
  background-color: #2A2A3B;
  border-radius: 8px;
  padding: 15px;
  margin-top: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.user-info-header {
  font-size: 1.25rem;
  font-weight: bold;
  color: #FF6B6B;
  margin-bottom: 10px;
}

.user-info-content {
  font-size: 1rem;
  color: #FFFFFF;
}
</style>
