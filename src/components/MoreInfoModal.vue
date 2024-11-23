<template>
    <BModal id="modal-center" centered size="lg" :title="store.moreInfo.content_title">
        <BRow>
            <BCol>
              <template v-for="(contentData, index) in store.moreInfo.content_data" :key="index">
                    <p v-if="index === 0">
                        {{ contentData }}
                    </p>
                </template>
            </BCol>
            <BCol>
              <template v-for="(contentData, index) in store.moreInfo.content_data" :key="index">
                    <p v-if="index === 1">
                        {{ contentData }}
                    </p>
                </template>
            </BCol>
            <BCol>
                <p>language: {{ store.moreInfo.lang_local_name }}</p>
                <p>score: {{ store.moreInfo.score }}</p>
                <p>failures: {{ store.moreInfo.failures }}</p>
                <p>total: {{ store.moreInfo.total_score }}</p>
            </BCol>
        </BRow>
      <!-- <img :src="moreInfo.avatarURL" alt="Dreamer Avatar" style="width: 75px; height: 75px;" /> -->
    </BModal>
</template>

<script setup>
import { onMounted } from 'vue';
import { useStore } from '../store';
import { storeToRefs } from 'pinia';
const store = useStore()

const { moreInfo } = storeToRefs(store)
    


</script>

<style>
#modal-center .modal-dialog {
  max-width: 90vw;
}

#modal-center .modal-content {
  background-color: #2A2A3B;
  color: #FFFFFF;
  border-radius: 8px;
  font-family: sans-serif;
  text-align: center;
  padding: 20px;
}

#modal-center .modal-header {
  background-color: #333344;
  color: #FF6B6B;
  font-size: 18px;
  border-bottom: none;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

#modal-center .modal-body {
  padding: 15px 0;
  font-size: 16px;
  color: #FFFFFF;
}

#modal-center .modal-body img {
  border-radius: 50%;
  margin-bottom: 10px;
  border: 2px solid #4CAF50;
}

#modal-center .modal-footer {
  background-color: #333344;
  border-top: none;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
}

#modal-center .close {
  color: #FF6B6B;
  opacity: 1;
}

#modal-center .close:hover {
  color: #FF5A5A;
}

#modal-center button.btn {
  background-color: #4CAF50;
  color: #FFFFFF;
  border: none;
  padding: 8px 15px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

#modal-center button.btn:hover {
  background-color: #3E8E41;
}</style>