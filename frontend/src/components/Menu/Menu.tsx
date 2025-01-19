import { Link } from "react-router";
import './Menu.css';

export default function Menu() {
    return (
        <ul>
            <li><Link to="/" >Home</Link></li>
            <li><Link to="/statements" >Statements</Link></li>
            <li><Link to="/transactions" >Transactions</Link></li>
        </ul>
    );
}