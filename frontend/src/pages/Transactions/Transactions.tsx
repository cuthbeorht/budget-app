import { useEffect, useState } from "react";

export default function Transactions() {
    
    const [transactions, setTransactions] = useState([]);
    
    useEffect(() => {
        
        async function fetchData() {
            const httpOptions = {
                method: "GET",
    
            }
            const response = await fetch("http://localhost:8000/transactions", httpOptions)
            const transactions = await response.json();
            setTransactions(transactions["transactions"]);
        }
        fetchData();        
    }, [transactions])

    return (
        <>
            <h1>Transactions</h1>
            <div>
                <ul>
                    {
                        transactions.map(tx => {
                            return <li>{tx.id}</li>
                        })
                    }
                </ul>
            </div>
        </>
    );
}