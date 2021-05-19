import axios from "axios";
import authHeader from "./auth-header";
import { refresh} from "./components/store/Actions/actions";
import store from "./components/store/store";
const baseURL = `http://127.0.0.1:8000/api/`;
const axiosInstance = axios.create({
    baseURL: baseURL,

})
axiosInstance.interceptors.request.use(config => {
    config.headers = authHeader();
    return config;
});
axiosInstance.interceptors.response.use(
    function (response) {
        return response;
    },
    async function (error) {
        const originalRequest = error.config;
        console.log(originalRequest)
        if (
            error.response.status === 401

        ) {
            await store.dispatch(refresh());
            originalRequest.headers['Authorization'] = `Bearer ${localStorage.getItem('access')}`
            console.log(originalRequest)
            return axiosInstance(originalRequest);
        }
        else if(error.response.status === 404){
            alert("Bad request")
             return Promise.reject(error);
        }
        else if(error.response.status === 403){
            alert("Permission denied")
             return Promise.reject(error);
        }
        else if(error.response.status === 400){
             return Promise.reject(error);
        }
        else {
            alert("Error")
             return Promise.reject(error);
        }

    }
);

export default axiosInstance;