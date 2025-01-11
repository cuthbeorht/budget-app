import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Budgeting from './Budgeting.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Budgeting />
  </StrictMode>,
)
