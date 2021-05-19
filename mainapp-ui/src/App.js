import './App.css';
import React, {useState, useEffect} from 'react';
import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import Owner from "./components/Models/Owner";
import Exhibition from "./components/Models/Exhibition";
import Artist from "./components/Models/Artist";
import ExhibitionHall from "./components/Models/ExhibitionHall";
import Artwork from "./components/Models/Artwork";
import LoginPage from "./login";
import SingUp from "./registration";
import MainPage from "./MainPage";

function App() {
  return (
    <div className="App">
        <Router>
            <MainPage />
            <Switch>
                <Route path="/owners" exact component={Owner}/>
                <Route path="/exhibitions" exact component={Exhibition}/>
                <Route path="/exhibition_halls" exact component={ExhibitionHall}/>
                <Route path="/artists" exact component={Artist}/>
                <Route path="/artworks" exact component={Artwork}/>
                <Route path="/login" exact component={LoginPage}/>
                <Route path="/register" exact component={SingUp}/>
            </Switch>
        </Router>
    </div>
  );
}

export default App;