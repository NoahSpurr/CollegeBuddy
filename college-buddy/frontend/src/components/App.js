import React, { Component } from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from "react-router-dom";
import SpacedRepetition from "./SpacedRepetition";


export default function App () {
    return (
        <Router>
            <Routes>
                <Route path='/' element={<SpacedRepetition/>}/>
            </Routes>
        </Router>
    );
}

console.log('New New Test...')
const root = ReactDOM.createRoot(document.getElementById('app'));
root.render(<App/>);