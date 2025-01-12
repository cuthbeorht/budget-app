import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'

import { BrowserRouter, Route, Routes } from 'react-router'
import Statements from './pages/Statements/Statements.tsx'
import Budgeting from './Budgeting.tsx'
import Home from './pages/Home/Home.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Budgeting />}>
          <Route index element={<Home />} />
          <Route path="/statements" element={<Statements />} />
        </Route>
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
