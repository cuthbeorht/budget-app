import { Outlet } from "react-router";
import Menu from "../../components/Menu/Menu";

export default function Home() {
    return (
        <div>
            <section>
                <Menu />
            </section>            
            <section>
                <Outlet />
            </section>
            
        </div>
    );
}