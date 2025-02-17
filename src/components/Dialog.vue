<template>
    <div class="text-center pa-4">
        <v-dialog v-model="dialog" transition="dialog-bottom-transition" fullscreen>
            <template v-slot:activator="{ props: activatorProps }">
                <v-btn class="open-dialog-button" prepend-icon="mdi-cog" size="small" text="Settings"
                    v-bind="activatorProps"></v-btn>
            </template>

            <v-card>
                <v-toolbar>
                    <v-btn icon="mdi-close" @click="dialog = false"></v-btn>

                    <v-toolbar-title>Settings</v-toolbar-title>

                    <v-spacer></v-spacer>

                    <v-toolbar-items>
                        <v-btn text="Save" variant="text" @click="dialog = false"></v-btn>
                    </v-toolbar-items>
                </v-toolbar>

                <v-row class="ma-0" justify="space-between" no-gutters>
                    <!-- Section 1 -->
                    <v-col class="pa-4" style="background-color: #f5f5f5;">
                        <v-card class="player-card mx-auto">
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
                                        <v-img :src="`/assets/flag${store.moreInfo.lang_id}.png`" class="flag-image"
                                            alt="Language Flag" />
                                    </div>
                                </div>

                                <div class="mt-3">
                                    <div>Birthdate: {{ new Date(store.dreamerInfo.birthdate).toLocaleDateString('en-GB',
                                        {
                                            day:
                                                '2-digit', month: 'short', year: 'numeric'
                                        }) }}</div>
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
                </v-row>
                <v-row class="ma-0" justify="space-between" no-gutters>
                    

                    <!-- Section 2 -->
                    <v-col class="pa-4" cols="6" style="background-color: #e8e8e8;">
                        <v-card class="contents-card mx-auto" max-width="344">
                            <template v-slot:title>
                                <h1 class="modal-header">Contents</h1>
                            </template>
                            <v-card-text>
                                <v-img class="thumbnail-art" height="200" :src="store.contentArt.thumbnail_url"
                                    cover></v-img>
                                <div class="text-center text-h5 font-weight-bold">
                                    {{ store.moreInfo.content_title }}
                                </div>
                                <div class="mt-3">
                                    <div>
                                        {{ store.moreInfo.content_description }}
                                    </div>
                                </div>
                            </v-card-text>
                            <v-card-actions>
                                <v-btn color="deep-purple-accent-4" text="Learn More" variant="text"></v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-col>

                    <!-- Section 3 -->
                    <v-col class="pa-4" cols="6" style="background-color: #dcdcdc;">
                        <v-card class="game-card mx-auto" max-width="344">
                            <template v-slot:title>
                                <h1 class="modal-header">Game Session</h1>
                            </template>
                            <v-card-text>
                                <div class="d-flex align-items-center mb-3">
                                    <div class="flag-container">
                                        <v-img :src="`/assets/flag${store.moreInfo.lang_id}.png`" class="flag-image"
                                            alt="Language Flag" />
                                    </div>
                                    <span class="text-h5">{{ store.moreInfo.lang_local_name }}</span>
                                </div>

                                <!-- Completed Status -->
                                <template>
                                    <div class="d-flex align-items-center mb-3">
                                        <div v-if="store.moreInfo.completed" class="tick-container me-2">
                                            <img src="/assets/check-tick-mark-in-green-circle.jpg" alt="Success Tick"
                                                class="tick-icon" />
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
            </v-card>
        </v-dialog>
    </div>
</template>

<script setup>
import { useStore } from '../store';
import { storeToRefs } from 'pinia';
import { ref } from 'vue'

const store = useStore();

const dialog = ref(false);

</script>

<style scoped>
/* Dialog Background */
.v-dialog {
    background-color: rgba(30, 30, 47, 0.9); /* Dark semi-transparent */
}

/* Card inside the modal */
.v-card {
    background-color: #2A2A3B !important; /* Dark background for consistency */
    color: #FFFFFF !important; /* White text */
}

/* Toolbar styling */
.v-toolbar {
    background-color: #333344 !important;
    color: #FFFFFF !important;
}

/* Close and Save buttons */
.v-btn {
    color: #FFFFFF !important;
}

.v-btn:hover {
    opacity: 0.8;
}

/* Section backgrounds */
.v-col {
    background-color: #2A2A3B !important; /* Darker tone */
}

/* Avatar and flag image */
.v-avatar,
.flag-image {
    border: 2px solid #FFFFFF;
}

/* Text headers */
.modal-header {
    color: #FFFFFF !important;
}

/* Customizing the "Learn More" buttons */
.v-card-actions .v-btn {
    color: #FF6B6B !important; /* Keep consistent with the red accent */
}
</style>
