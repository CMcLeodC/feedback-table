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
              <div>name: {{ store.dreamerInfo.name }}</div>
              <p class="text-h4 font-weight-black">be•nev•o•lent</p>
              <p>adjective</p>
              <div class="text-medium-emphasis">
                well meaning and kindly.<br />
                "a benevolent smile"
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn color="deep-purple-accent-4" text="Learn More" variant="text"></v-btn>
            </v-card-actions>
          </v-card>
        </v-col>

        <!-- Card 2 -->
        <v-col cols="12" md="4">
          <v-card class="mx-auto my-12" max-width="374">
            <template v-slot:title>
              Counter
            </template>

            <v-img height="250" src="https://cdn.vuetifyjs.com/images/cards/cooking.png" cover></v-img>
            <v-card-item>
              <v-card-title>Cafe Badilico</v-card-title>
              <v-card-subtitle>
                <span class="me-1">Local Favorite</span>
                <v-icon color="error" icon="mdi-fire-circle" size="small"></v-icon>
              </v-card-subtitle>
            </v-card-item>
            <v-card-text>
              <v-row align="center" class="mx-0">
                <v-rating
                  :model-value="4.5"
                  color="amber"
                  density="compact"
                  size="small"
                  half-increments
                  readonly
                ></v-rating>
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
              <v-btn
                color="deep-purple-lighten-2"
                block
                border
              ></v-btn>
            </v-card-actions>
          </v-card>
        </v-col>

        <!-- Card 3 -->
        <v-col cols="12" md="4">
          <v-card class="mx-auto" max-width="400">
            <v-layout>
              
              <v-main>
                <v-container>
                  <v-row dense>
                    <v-col cols="12">
                      
                      <v-card color="#385F73">
                        <template v-slot:title>
              Counter
            </template>
                        <v-card-title class="text-h5">Unlimited music now</v-card-title>
                        <v-card-subtitle>
                          Listen to your favorite artists and albums whenever and wherever, online and offline.
                        </v-card-subtitle>
                        <v-card-actions>
                          <v-btn text="Listen Now" variant="text"></v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-col>
                    <v-col cols="12">
                      <v-card color="#1F7087">
                        <div class="d-flex flex-no-wrap justify-space-between">
                          <div>
                            <v-card-title class="text-h5">Supermodel</v-card-title>
                            <v-card-subtitle>Foster the People</v-card-subtitle>
                            <v-card-actions>
                              <v-btn
                                class="ms-2"
                                size="small"
                                text="START RADIO"
                                variant="outlined"
                              ></v-btn>
                            </v-card-actions>
                          </div>
                          <v-avatar class="ma-3" rounded="0" size="125">
                            <v-img src="https://cdn.vuetifyjs.com/images/cards/foster.jpg"></v-img>
                          </v-avatar>
                        </div>
                      </v-card>
                    </v-col>
                    <v-col cols="12">
                      <v-card color="#952175">
                        <div class="d-flex flex-no-wrap justify-space-between">
                          <div>
                            <v-card-title class="text-h5">Halcyon Days</v-card-title>
                            <v-card-subtitle>Ellie Goulding</v-card-subtitle>
                            <v-card-actions>
                              <v-btn class="ms-2" icon="mdi-play" variant="text"></v-btn>
                            </v-card-actions>
                          </div>
                          <v-avatar class="ma-3" rounded="0" size="125">
                            <v-img src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"></v-img>
                          </v-avatar>
                        </div>
                      </v-card>
                    </v-col>
                  </v-row>
                </v-container>
              </v-main>
            </v-layout>
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
const { cards, dreamerInfo } = storeToRefs(store);

// const showModal = ref(false);

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
  color: #FFFFFF;
}

.vuetify-modal-container.v-card {
  position: fixed !important;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>