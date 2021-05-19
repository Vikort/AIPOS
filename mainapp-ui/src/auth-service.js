import axios from "axios";
import {BehaviorSubject} from "rxjs";
const API_URL = "http://localhost:8000/api/";

class AuthService {



    register(username, password) {
        return axios.post(API_URL + "register", {
            username,
            password
        });
    }

}

export default new AuthService();