import { useState } from 'react';
import './Budgeting.css'

const links = [{
  name: "statements",
  href: "/statements"
}];

export default function Budgeting() {
  const [budgetLinks, _] = useState(links)

  return (
    <>
     <div>
        {
          budgetLinks.map(link => <a href={link.href}>{link.name}</a>)
        }
      </div> 
    </>
  )
}
