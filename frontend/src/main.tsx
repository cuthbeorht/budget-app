import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'

import { BrowserRouter, Route, Routes } from 'react-router'
import Statements from './pages/Statements/Statements.tsx'
import Budgeting from './Budgeting.tsx'
import Home from './pages/Home/Home.tsx'
import Transactions from './pages/Transactions/Transactions.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Budgeting />}>
          <Route index element={<Home />} />
          <Route path="/statements" element={<Statements />} />
          <Route path="/transactions" element={<Transactions />} />
        </Route>
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
