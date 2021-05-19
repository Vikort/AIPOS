import React, {useState, useEffect, useRef} from 'react';
import './App.css';
import {Link} from "react-router-dom";
import {useDispatch, useSelector} from "react-redux";
import {logout} from "./components/store/Actions/actions";


function MainPage() {
    const isAuthenticated = useSelector(state => state.isAuthenticated)
    const dispatch = useDispatch();
    const handleClick = (e) => {
        dispatch(logout())
    }
    const authLinks = (
        <Link className="btn btn-dark btn-lg" onClick={handleClick}>Logout</Link>
    );
    const guestLinks = (
        <Link className="btn btn-dark btn-lg" to={{pathname: `/login`}}>Login</Link>
    );


    return (
                <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                    <div className="container-fluid">
                    <ul className="navbar-nav mr-auto">
                        <li className="nav-item"><Link className="nav-link" to={{pathname: `/owners`}}> Owners</Link></li>
                        {isAuthenticated ? <li className="nav-item"><Link className="nav-link" to={{pathname: `/exhibitions`}}>Exibitions</Link></li> : <li className="nav-item"><Link className="nav-link">Иди представься! :) </Link></li>}
                        {isAuthenticated ? <li className="nav-item"><Link className="nav-link" to={{pathname: `/artists`}}>Artists</Link></li> : <li className="nav-item"><Link className="nav-link">Иди представься! :) </Link></li>}
                        {isAuthenticated ? <li className="nav-item"><Link className="nav-link" to={{pathname: `/artworks`}}>Artworks</Link></li> : <li className="nav-item"><Link className="nav-link">Иди представься! :) </Link></li>}
                        {isAuthenticated ? <li className="nav-item"><Link className="nav-link" to={{pathname: `/exhibition_halls`}}>Exhibition Halls</Link></li> : <li className="nav-item"><Link className="nav-link">Иди представься! :) </Link></li>}
                    </ul>
                    {isAuthenticated ? authLinks : guestLinks}

                    </div>
                </nav>
    );
}


export default MainPage;