<!-- frontend/src/components/ui/BootstapAccordeon.vue -->

<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{
  id: string | number
  isOpen?: boolean
}>()

const isOpen = ref(props.isOpen || false)

const toggle = () => {
  isOpen.value = !isOpen.value
}

// --- Lógica de Animación (JavaScript Hooks) ---

// 1. Antes de empezar a abrir: forzar altura 0
const beforeEnter = (el: Element) => {
  const htmlEl = el as HTMLElement
  htmlEl.style.height = '0'
  htmlEl.style.overflow = 'hidden' // Evitar scrollbar durante la animación
}

// 2. Al empezar a abrir: calcular altura real y animar
const enter = (el: Element, done: () => void) => {
  const htmlEl = el as HTMLElement
  // Forzar un reflow para que el navegador registre el height 0 inicial
  void htmlEl.offsetHeight 
  
  // Establecer la altura al scrollHeight (altura total del contenido)
  htmlEl.style.height = `${htmlEl.scrollHeight}px`
  
  // Escuchar el final de la transición CSS
  htmlEl.addEventListener('transitionend', done, { once: true })
}

// 3. Al terminar de abrir: limpiar estilos
const afterEnter = (el: Element) => {
  const htmlEl = el as HTMLElement
  htmlEl.style.height = '' // Volver a 'auto'
  htmlEl.style.overflow = ''
}

// 4. Antes de empezar a cerrar: fijar la altura actual explicitamente
const beforeLeave = (el: Element) => {
  const htmlEl = el as HTMLElement
  htmlEl.style.height = `${htmlEl.scrollHeight}px`
  htmlEl.style.overflow = 'hidden'
}

// 5. Al empezar a cerrar: animar a 0
const leave = (el: Element, done: () => void) => {
  const htmlEl = el as HTMLElement
  // Forzar un reflow
  void htmlEl.offsetHeight 
  // Animar a 0
  htmlEl.style.height = '0'
  
  htmlEl.addEventListener('transitionend', done, { once: true })
}

// 6. Al terminar de cerrar: limpiar estilos
const afterLeave = (el: Element) => {
  const htmlEl = el as HTMLElement
  htmlEl.style.height = ''
  htmlEl.style.overflow = ''
}
</script>

<template>
  <div class="accordion-item mb-2 border rounded shadow-sm">
    <h2 class="accordion-header">
      <button
        class="accordion-button py-2"
        :class="{ collapsed: !isOpen }"
        type="button"
        @click="toggle"
        :aria-expanded="isOpen"
      >
        <slot name="header"></slot>
      </button>
    </h2>

    <Transition
      name="accordion"
      @before-enter="beforeEnter"
      @enter="enter"
      @after-enter="afterEnter"
      @before-leave="beforeLeave"
      @leave="leave"
      @after-leave="afterLeave"
    >
      <div v-show="isOpen" class="accordion-collapse">
        <div class="accordion-body p-0">
          <slot name="content"></slot>
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
.accordion-button:focus { 
  box-shadow: none; 
}
.accordion-button:not(.collapsed) {
  background-color: transparent;
  color: inherit;
}

/* --- Estilos de Animación CSS --- */

/* Esta clase se aplica al elemento durante TODA la transición */
.accordion-enter-active,
.accordion-leave-active {
  /* Usamos la misma duración y curva que Bootstrap (aprox) */
  transition: height 0.35s ease;
}

/* Rotación del icono (Bootstrap style) */
.accordion-button::after {
  transition: transform 0.2s ease-in-out;
}
.accordion-button.collapsed::after {
  transform: rotate(0deg);
}
.accordion-button:not(.collapsed)::after {
  transform: rotate(-180deg);
}
</style>