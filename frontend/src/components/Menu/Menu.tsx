import { Link } from "react-router";

export default function Menu() {
    return (
        <nav>
            <Link to="/" >Home</Link>
            <Link to="/statements" >Statements</Link>
        </nav>
    );
}