<template>
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
            <th>Actions</th> <!-- Actions column -->
        </tr>
    </thead>
    <tbody>
        <tr v-for="(item, index) in feedbackList" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ item.created_at }}</td>
            <td>
                <img :src="item.dreamer_avatar" alt="Dreamer Avatar" class="avatar" />
            </td>
            <td>{{ item.dreamer_name }}</td>
            <td>{{ item.user_name }}</td>
            <td>{{ item.content_title }}</td>
            <td>{{ item.level_name }}</td>
            <td>{{ item.duration }}</td>
            <td>{{ item.score }}</td>
            <td>
                <button @click="handleAction(item)">Action</button>
            </td>
        </tr>
    </tbody>
</table>

</template>

<script>
export default {
    props: {
        feedbackList: Object,
        sortBy: String,
        sortDesc: Boolean
    }
}
</script>
<style>
table th, td {
    color: white;
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
</style>