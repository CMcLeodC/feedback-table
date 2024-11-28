<template>
  <div v-if="store.showModal" class="modal-overlay" @click="closeModal"></div>

  <v-card v-if="store.showModal" class="vuetify-modal-container mx-auto" max-width="1700">
    <v-container fluid>
      <v-row dense justify="space-between">
        <!-- Card 1 -->
        <v-col cols="12" md="4">
          <v-card class="mx-auto" max-width="344">
            <template v-slot:title>
              Player
            </template>
            <v-card-text>
              <v-avatar size="100" class="mx-auto mb-4">
                <v-img :src="store.handleAvatarUrl(store.dreamerInfo.avatar)" alt="Player Avatar" />
              </v-avatar>
              <div class="text-center text-h5 font-weight-bold">
                {{ store.dreamerInfo.name }}
                <v-icon v-if="store.dreamerInfo.local_flag" color="success" icon="mdi-flag" class="ms-2" />
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
                <div>User: {{ store.userInfo.name }}</div>
                <div>User email: {{ store.userInfo.email }}</div>
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn color="deep-purple-accent-4" text="Learn More" variant="text"></v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        {{ console.log("hello", store.dreamerInfo.name) }}
        <!-- Card 2 -->
        <!-- <v-col cols="12" md="4">
          <v-card class="mx-auto my-12" max-width="374">
            <template v-slot:title>
              Counter
            </template>

            <v-img height="250" :src="store.contentArt.thumbnail_url" cover></v-img>
            <v-card-item>
              <v-card-title>Cafe Badilico</v-card-title>
              <v-card-subtitle>
                <span class="me-1">Local Favorite</span>
                <v-icon color="error" icon="mdi-fire-circle" size="small"></v-icon>
              </v-card-subtitle>
            </v-card-item>
            <v-card-text>
              <v-row align="center" class="mx-0">
                <v-rating :model-value="4.5" color="amber" density="compact" size="small" half-increments
                  readonly></v-rating>
                <div class="text-grey ms-4">4.5 (413)</div>
              </v-row>
              <div class="my-4 text-subtitle-1">$ • Italian, Cafe</div>
              <div>
                Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating.
              </div>
            </v-card-text>
            <v-divider class="mx-4 mb-1"></v-divider>
            <v-card-title>Tonight's availability</v-card-title>
            <div class="px-4 mb-2">
              <v-chip-group selected-class="bg-deep-purple-lighten-2">
                <v-chip>5:30PM</v-chip>
                <v-chip>7:30PM</v-chip>
                <v-chip>8:00PM</v-chip>
                <v-chip>9:00PM</v-chip>
              </v-chip-group>
            </div>
            <v-card-actions>
              <v-btn color="deep-purple-lighten-2" block border></v-btn>
            </v-card-actions>
          </v-card>
        </v-col> -->

        <v-col cols="12" md="4">
          <v-card class="mx-auto" max-width="344">
            <template v-slot:title>
              Player
            </template>
            <v-card-text>
              <v-img height="250" :src="store.contentArt.thumbnail_url" cover></v-img>
              <div class="text-center text-h5 font-weight-bold">
                {{ store.moreInfo.content_title }}
                <v-icon v-if="store.dreamerInfo.local_flag" color="success" icon="mdi-flag" class="ms-2" />
              </div>
              <div class="mt-3">
                <div>
                  {{  store.moreInfo.content_description }}
                </div>
              </div>
              <div class="mt-3 d-flex justify-space-between">
                <div>Coins: {{ store.dreamerInfo.coins }}</div>
                <div>Gems: {{ store.dreamerInfo.gems }}</div>
              </div>
              <div class="mt-3">
                <div>User: {{ store.userInfo.name }}</div>
                <div>User email: {{ store.userInfo.email }}</div>
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn color="deep-purple-accent-4" text="Learn More" variant="text"></v-btn>
            </v-card-actions>
          </v-card>
        </v-col>

        <!-- Card 3 -->
        <v-col cols="12" md="4">
          <v-card class="mx-auto game-card" max-width="344">
            <template v-slot:title>
              Game
            </template>
            <v-card-text>
              <!-- Language Info: Flag and Name -->
              <div class="d-flex align-items-center mb-3">
                <v-avatar size="32" class="me-2">
                  <v-img :src="`/path/to/flags/${store.moreInfo.lang_id}.png`" alt="Language Flag" />
                </v-avatar>
                <span class="text-h5">{{ store.moreInfo.lang_local_name }}</span>
              </div>

              <!-- Completed Status -->
              <div class="d-flex align-items-center mb-3">
                <v-icon v-if="store.moreInfo.completed" color="success" size="32" class="me-2">mdi-check-circle</v-icon>
                <v-icon v-else color="grey" size="32" class="me-2">mdi-circle-outline</v-icon>
                <span class="text-h6">Completed</span>
              </div>

              <!-- Time and Score -->
              <div class="mt-3">
                <div>Time: {{ store.moreInfo.time }}</div>
                <div>Score: {{ store.moreInfo.score }}</div>
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

<style>
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
  background-color: #2A2A3B;
  color: #FFFFFF;
}

.vuetify-modal-container.v-card {
  background-color: #2A2A3B !important; /* Ensures consistency if card styles override */
  position: fixed !important;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
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

.v-col .v-card.player-card, 
.v-col .v-card.counter-card, 
.v-col .v-card.game-card {
  border: 2px solid #3A3A4D; /* Light border for separation */
  padding: 20px;              /* Add padding for better spacing */
  border-radius: 10px;        /* Rounded corners */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);  /* Subtle shadow for depth */
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

/* Counter card specific styling */
.v-col .v-card.counter-card {
  background-color: #1E1E2F; /* Matches table's even rows */
}

/* Game card specific styling */
.v-col .v-card.game-card {
  background-color: #262637; /* Slightly lighter than modal for contrast */
}

.v-card-title, .v-card-text {
  color: #CCCCCC !important;
}

.v-card-title {
  color: #FFFFFF;
}

.v-card-text div {
  margin-bottom: 10px;
  color: #CCCCCC;
}

.v-btn {
  background-color: #333344; /* Button background inside modal */
  color: #FFFFFF;
  border: none;
}

.v-btn:hover {
  background-color: #444455; /* Subtle hover effect for buttons */
  transition: background-color 0.2s ease;
}

.v-icon {
  vertical-align: middle;
}
</style>
