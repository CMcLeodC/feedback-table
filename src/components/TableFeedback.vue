<template>
    <div>
        <table class="table">
            <thead>
                <tr>
                    <th>#</th>
                    <th @click="sortTable('created_at')">
                        Date
                        <span :class="['arrow', sortBy === 'created_at' && !sortDesc ? 'active' : '']">▲</span>
                        <span :class="['arrow', sortBy === 'created_at' && sortDesc ? 'active' : '']">▼</span>
                    </th>
                    <th>Avatar</th>
                    <th @click="sortTable('dreamer_name')">
                        Dreamer
                        <span :class="['arrow', sortBy === 'dreamer_name' && !sortDesc ? 'active' : '']">▲</span>
                        <span :class="['arrow', sortBy === 'dreamer_name' && sortDesc ? 'active' : '']">▼</span>
                    </th>
                    <th @click="sortTable('user_name')">
                        User
                        <span :class="['arrow', sortBy === 'user_name' && !sortDesc ? 'active' : '']">▲</span>
                        <span :class="['arrow', sortBy === 'user_name' && sortDesc ? 'active' : '']">▼</span>
                    </th>
                    <th @click="sortTable('content_title')">
                        Content
                        <span :class="['arrow', sortBy === 'content_title' && !sortDesc ? 'active' : '']">▲</span>
                        <span :class="['arrow', sortBy === 'content_title' && sortDesc ? 'active' : '']">▼</span>
                    </th>
                    <th @click="sortTable('level_name')">
                        Difficulty Level
                        <span :class="['arrow', sortBy === 'level_name' && !sortDesc ? 'active' : '']">▲</span>
                        <span :class="['arrow', sortBy === 'level_name' && sortDesc ? 'active' : '']">▼</span>
                    </th>
                    <th @click="sortTable('duration')">
                        Time (Seconds)
                        <span :class="['arrow', sortBy === 'duration' && !sortDesc ? 'active' : '']">▲</span>
                        <span :class="['arrow', sortBy === 'duration' && sortDesc ? 'active' : '']">▼</span>
                    </th>
                    <th @click="sortTable('score')">
                        Score
                        <span :class="['arrow', sortBy === 'score' && !sortDesc ? 'active' : '']">▲</span>
                        <span :class="['arrow', sortBy === 'score' && sortDesc ? 'active' : '']">▼</span>
                    </th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in feedbackList" :key="index">
                    <td>{{ index + 1 + (currentPage - 1) * perPage }}</td>
                    <td>{{ item.created_at }}</td>
                    <td>
                        <img :src="store.handleAvatarUrl(item.dreamer_avatar)" alt="Dreamer Avatar" class="avatar" />
                    </td>
                    <td>{{ item.dreamer_name }}</td>
                    <td>{{ item.user_name }}</td>
                    <td>{{ item.content_title }}</td>
                    <td>{{ item.level_name }}</td>
                    <td>{{ item.duration }}</td>
                    <td>{{ item.score }}</td>
                    <td>
                        <button @click="store.openModalWithID(item.id)">Action</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <div class="pagination">
            <button :disabled="currentPage === 1" @click="prevPage">Previous</button>
            <span>Page {{ currentPage }} of {{ pageCount }}</span>
            <button :disabled="currentPage === pageCount" @click="nextPage">Next</button>
        </div>
    </div>

</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useStore } from '../store';
import { storeToRefs } from 'pinia';
const store = useStore()

const { sortBy, feedbackList, sortDesc, currentPage, pageCount, perPage } = storeToRefs(store)

const nextPage = () => {
    if (currentPage.value < pageCount.value) {
        currentPage.value++;
        store.fetchFeedback();
        console.log(currentPage.value);
        
    }
};

const prevPage = () => {
    if (currentPage.value > 1) {
        currentPage.value--;
        store.fetchFeedback();
        console.log(currentPage.value);
    }
};

const sortTable = (field) => {
    if (sortBy.value === field) {
        sortDesc.value = !sortDesc.value; // Toggle sort direction
    } else {
        sortBy.value = field;
        sortDesc.value = false; // Default to ascending
    }
    currentPage.value = 1; // Reset to the first page
    store.fetchFeedback();
};

</script>
<style>
table th,
td {
    color: white !important;
}

.arrow {
    color: gray;
    font-size: 0.75em;
    margin-left: 4px;
}

.active {
    color: white;
}

.arrow:hover {
    cursor: pointer;
}

.pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    margin: 20px 0;
}

.pagination button {
    padding: 8px 12px;
    font-size: 14px;
    font-weight: bold;
    color: #FFFFFF;
    background-color: #333344;
    border: 1px solid #FFFFFF;
    border-radius: 5px;
    transition: background-color 0.3s, transform 0.2s;
}

.pagination button:disabled {
    color: #777777;
    background-color: #2A2A3B;
    cursor: not-allowed;
    border-color: #555555;
}

.pagination button:hover:not(:disabled) {
    background-color: #4CAF50;
    color: #FFFFFF;
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

.pagination span {
    font-size: 14px;
    font-weight: bold;
    color: #FFFFFF;
}
</style>