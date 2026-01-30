import { BrowserRouter, Routes, Route } from "react-router-dom";

function Home(){
    return <h2>Home</h2>
}

export function AppRoutes(){
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
            </Routes>
        </BrowserRouter>
    )
}