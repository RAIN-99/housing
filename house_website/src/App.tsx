import {Route, Routes} from 'react-router-dom'
import {HousesPage} from './pages/HousesPage'
import {Analytics} from './pages/Analytics'
import {Navigation} from './components/Navigation'
import { MainPage } from './pages/MainPage'
import {Login} from "./pages/Login"
function App() {
  return (
    <>
      <Navigation />
      <Routes>
        <Route path="/" element={ <MainPage /> } />
        <Route path="/login" element={ <Login /> } />
        <Route path="/houses/:area" element={ <HousesPage /> } />
        <Route path="/analytics" element={ <Analytics /> } />
      </Routes>
    </>
  )
}

export default App;
