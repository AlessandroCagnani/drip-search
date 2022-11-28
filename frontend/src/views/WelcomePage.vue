<template>

</template>

<script>
import SvgBackground from "@/components/SvgBackground";

import {nextSection} from '../js/WelcomePage/welcome.js';


export default {
  name: "WelcomePage",
  components: {
    SvgBackground
  },
  data() {
    return {
      // Make sure to put images in 1:1 aspect ratio
      sections: [{
        title: "Section A",
        src: "/assets/covers/cover1.png"
      },
        {
          title: "Section B",
          src: "/assets/covers/cover2.png"
        },
        {
          title: "Section C",
          src: "/assets/covers/cover3.png"
        },
        {
          title: "Section D",
          src: "/assets/covers/cover4.png"
        }
      ],
      activeSectionIndex: 0,
    }
  },
  computed: {
    activeSection() {
      return this.sections[this.activeSectionIndex % this.sections.length]
    }
  },
  mounted() {
    setInterval(() => this.nextSection(), 5000);
        //add an evnetlistener for mouse
        this.$el.addEventListener('mousemove', this.onMouseMove);
        this.$el.addEventListener('resize', this.onResize);
  },
  methods: {
    nextSection,
    onMouseMove(e) {
      const spansSlow = document.querySelectorAll('.spanSlow');
      const spansFast = document.querySelectorAll('.spanFast');
      let width = window.innerWidth;
      let normalizedPosition = e.pageX / (width / 2) - 1;
      let speedSlow = 100 * normalizedPosition;
      let speedFast = 200 * normalizedPosition;
      spansSlow.forEach((span) => {
        span.style.transform = `translate(${speedSlow}px)`;
      });
      spansFast.forEach((span) => {
        span.style.transform = `translate(${speedFast}px)`
      })
    }
  },

};

</script>

<style scoped>

</style>
