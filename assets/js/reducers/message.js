import _ from 'lodash'

const initialState = []

export default function messageReducer(state = initialState, action) {
  switch(action.type) {
    case 'MESSAGES_RECEIVED':
      console.log("I got messages: ", action.payload, state)
      return _.unionBy(action.payload, state, 'id')
    case 'MESSAGE_RECEIVED':
      return _.unionBy([action.payload], state, 'id')
    default:
      return state
  }
}
