
export const history = {
  state: {
    histories: []
  },
  mutations: {
    pushHis(state, value) {
      state.histories.push(value)
    },
    popHis(state) {
      state.histories.pop()
    },
    updateHis(state, value) {
      state.histories.pop()
      state.histories.push(value)
    }
  },
  getters: {
    showHistories(state) {
      return state
    }
  }
}
