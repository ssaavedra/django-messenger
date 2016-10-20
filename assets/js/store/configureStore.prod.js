import { createStore, applyMiddleware } from 'redux'
import createSagaMiddleware from 'redux-saga'

import rootReducer from '../reducers'
import rootSaga from '../sagas'

export default function configureStore (initialState) {
  const sagaMiddleware = createSagaMiddleware()
  const createStoreWithMiddleware = applyMiddleware(sagaMiddleware)(createStore)
  sagaMiddleware.run(rootSaga)
  
  return createStoreWithMiddleware(rootReducer, initialState)
  // return createStore(rootReducer, initialState)
}
