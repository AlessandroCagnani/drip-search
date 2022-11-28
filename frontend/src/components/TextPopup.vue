<template>
  <button
    v-if="showButton"
    @click="show"
  >
    <worldinfo class="button-svg" />
  </button>

  <Transition
    id="outertransition"
    name="fade"
  >
    <div
      v-show="isShown"
      id="back"
      class="back"
    >
      <Transition
        id="innertransition"
        name="fade"
      >
        <div
          v-show="isShown"
          class="text-popup"
        >
          <h1 id="popup-title">
            {{ title }}
          </h1>
          <!-- eslint-disable vue/no-v-html -->
          <span
            class="textBody"
            v-html="description"
          />
          <!--eslint-enable-->
          <div class="button-box">
            <button
              id="accept"
              @click="hide();executeCallback()"
            >
              Ok
            </button>
          </div>
        </div>
      </Transition>
    </div>
  </Transition>
</template>

<script>
import worldinfo from "@/assets/world_info.svg";
import {show, hide, executeCallback} from "@/js/ProfilePage/textpopup.js";

export default {
  name: 'TextPopup',
  components: {
    worldinfo
  },
  props: {
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    callback: {
          type: Function,
          default: () => {
            return {}
          }
        },
    autoOpen: {
      type: Boolean,
      required: false,
      default: false
    },
    showButton: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      isShown: false,
    }
  },
  mounted() {
    if (this.autoOpen) {
      this.show();
    }
  },
  methods: {
    show,
    hide,
    executeCallback,
  },

}
</script>

<style scoped>

</style>