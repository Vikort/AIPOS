import React, {useState, useEffect} from 'react';
import './App.css';
import axios from "axios";
import {Link, Redirect} from 'react-router-dom'

function SingUp({match}) {
    const [formData, setFormData] = useState({username: '', password: ''});
    const [redirect, setRedirect] = useState(false)
    const apiUrl = "http://127.0.0.1:8000/api/register";

    function register(username, password)
    {
        return axios.post(apiUrl, {
            username,
            password
        });
    }
    const saveUser = (e) => {
        e.preventDefault();
        debugger;
        register(formData.username, formData.password).then(response => {
            setRedirect(true)
        }).catch(err => {
            if (err.response) {
                alert("Bad request")
            } else if (err.request) {
                alert("Error")
            }
        })
    }
    const onChange = (e) => {
        e.persist();
        debugger;
        setFormData({...formData, [e.target.name]: e.target.value});
    }
    if (redirect) {
        return <Redirect to={{pathname: `/login`}}/>
    }
    return (
        <div>
            <form onSubmit={saveUser}>
                <input type="hidden" name="csrfmiddlewaretoken"
                       value="0pmpXbOsJcizwf95KkMx2zLtTewOy8CTVHQFqn3JRsSoWPoHqkkWpXktslABmAAC"/>
                <div className="form-outline mb-4" style={{'margin-left': '500px'}}>
                    <input type="text" name="username" className="input" placeholder="Username"
                           maxLength="100" required
                           id="id_username" onChange={onChange}/>
                </div>

                <div className="form-outline mb-4" style={{'margin-left': '500px'}}>
                    <input type="password" name="password" className="input" placeholder="Password" maxLength="100"
                           required
                           id="password" onChange={onChange}/>
                </div>

                <input className='btn btn-outline-dark btn-lg btn-block mb-4' style={{'margin-left': '700px'}}
                       type="submit" value="Sign up" text=""/>
            </form>
        </div>
    );

}

export default SingUp;