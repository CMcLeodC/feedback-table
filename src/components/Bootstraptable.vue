<!-- <template>

<BContainer>
        <BRow>
          <BCol>
            <div class="overflow-auto">
              <b-pagination v-model="props.currentPage" :total-rows="props.totalRows" :per-page="props.perPage" aria-controls="my-table"
                align="center" @update:model-value="fetchFeedback" />

              <p class="mt-3 text-center">Current Page: {{ props.currentPage }}</p>
              {{ sortBy }}
              <BTable id="my-table" :items="feedbackList" :fields="props.fields" striped hover
                :sort-by="[{ key: sortBy, order: sortDesc }]">
                <template #cell(#)="data">
                  {{ data.index + 1 }}
                </template>
                <template #cell(dreamer_avatar)="data">
                  <img :src="handleAvatarUrl(data.item.dreamer_avatar)" alt="Dreamer Avatar"
                    style="width: 50px; height: 50px;" />
                </template>
                <template #cell(actions)="data">
                  <BButton v-b-modal.modal-center @click="openModalWithID(data.item.id)">More Info</BButton>
                </template>
                <template #cell(level_name)="data">
                  {{ data.item.level_name.charAt(0).toUpperCase() + data.item.level_name.slice(1) }}
                </template>
                <template #cell(score)="data">
                  {{ data.item.score }}/{{ data.item.total_score }}
                </template>
              </BTable>
              <!-- <b-pagination v-model="props.currentPage" :total-rows="props.totalRows" :per-page="props.perPage" aria-controls="my-table"
                align="center" @update:model-value="fetchFeedback" />

              <p class="mt-3 text-center">Current Page: {{ props.currentPage }}</p> -->
            </div>
          </BCol>
        </BRow>
      </BContainer>
</template>

<script setup>
import { BCol, BContainer, BRow, BTable } from 'bootstrap-vue-next'

const props = defineProps({
        feedbackList: Array,
        fields: Array,
        sortBy: String,
        sortDesc: Boolean,
        currentPage: Number,
        perPage: Number,
        totalRows: Number,
        fetchFeedback: Array,
        handleAvatarUrl: Function
    })
</script>

<style></style> -->