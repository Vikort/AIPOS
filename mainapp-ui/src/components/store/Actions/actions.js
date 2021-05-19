import {
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    LOGOUT, REFRESH, REFRESH_FAIL,
} from "../Constants/constants";

import axios from "../../../axios";
import axiosInstance from "../../../axios";

const API_URL = "http://localhost:8000/api/";
export const login = (username, password) => async dispatch => {
    const response = await axios
        .post(API_URL + "token/obtain", {
            username,
            password
        })
        .then(response => {
            dispatch({
                type: LOGIN_SUCCESS,
                payload: response.data,
            });
        }).catch(err => {
            dispatch({
                type: LOGIN_FAIL
            })
        });
    console.log("login action creater")


};
export const refresh = () => async dispatch => {
    // const response = await axios
    //     .post(API_URL + "token/refresh", {
    //         refresh: localStorage.getItem("refresh")
    //     })
    const response = await axios
            .post(API_URL + "token/refresh", {
                refresh: localStorage.getItem("refresh")
            })
        .then(response => {
            dispatch({
                type: REFRESH,
                payload: response.data,
            });
        }).catch(err => {
            dispatch({
                type: REFRESH_FAIL
            })
        });
    console.log("refresh action creater")
}

export const logout = () => (dispatch) => {
    console.log("logout action creater")
    dispatch({
        type: LOGOUT,
    });
};