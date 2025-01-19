import { useEffect, useState } from "react";

interface Transaction {
    id: string;
    creditCardNumber: string;
    dateRecorded: string;
    datePosted: string;
    amount: number;
    description?: string;
}

export default function Transactions() {
    
    const [transactions, setTransactions] = useState<Transaction[]>([]);
    
    useEffect(() => {
        
        async function fetchData() {
            const httpOptions = {
                method: "GET",
    
            }
            const response = await fetch("http://localhost:8000/transactions", httpOptions)
            const transactionsJson = await response.json();
            const transactions: Transaction[] = transactionsJson.transactions.map((tx: unknown) => {return {
                id: tx.id,
                creditCardNumber: tx.credit_card_number,
                dateRecorded: tx.transaction_date,
                datePosted: tx.date_posted,
                amount: tx.transaction_amount,
                description: tx.description
            }});
            setTransactions(transactions);
        }
        fetchData();        
    }, [])

    return (
        <>
            <h1>Transactions</h1>
            <div>
                <table>
                    <thead>
                    <tr>
             
                        <td>Card Number</td>
                        <td>Date Recorded</td>
                        <td>Date Posted</td>
                        <td>Amount</td>
                        <td>Description</td>
                 
                    </tr>
                    </thead>
                    <tbody>
                    {
                        transactions.map((tx: Transaction) => {
                            return (
                                <tr key={tx.id}>
                                    <td>{tx.creditCardNumber}</td>                                    
                                    <td>{tx.dateRecorded}</td>
                                    <td>{tx.datePosted}</td>
                                    <td>{tx.amount}</td>
                                    <td>{tx.description}</td>                                    
                                </tr>
                            );
                        })
                    }
                    </tbody>
                </table>
            </div>
        </>
    );
}