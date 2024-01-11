import { defineStore } from 'pinia'

export const useFormIdStore = defineStore('formID', {
  state: () => {
    return {
      formDniCifColaborador: ''
    }
  }
})
