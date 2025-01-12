import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Budgeting from './Budgeting.tsx'
import { BrowserRouter, Route, Routes } from 'react-router'
import Home from './pages/Home/Home.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/statements" element={<Budgeting />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
