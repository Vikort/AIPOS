import {
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    LOGOUT, REFRESH, REFRESH_FAIL,
} from "../Constants/constants";

const access = localStorage.getItem("access")
const initialState = {
    access: localStorage.getItem("access"),
    refresh: localStorage.getItem("refresh"),
    isAuthenticated: !!access
}
export default function (state = initialState, action) {
    const {type, payload} = action;
    switch (type) {
        case LOGIN_SUCCESS:
            localStorage.setItem("access", payload.access);
            localStorage.setItem("refresh", payload.refresh);
            return {
                ...state,
                isAuthenticated: true,
                access: payload.access,
                refresh: payload.refresh
            }
        case LOGIN_FAIL:
            alert("Fail")
            return {
                ...state,
                isAuthenticated: false,
                access: null,
                refresh: null

            }
        case REFRESH_FAIL:
            return {
                ...state,
                isAuthenticated: false,
                access: null,
                refresh: null

            }
        case LOGOUT:
            localStorage.removeItem("access")
            localStorage.removeItem("refresh")
            return {
                ...state,
                isAuthenticated: false,
                access: null,
                refresh: null

            }
        case REFRESH:
            localStorage.removeItem("access")
            localStorage.setItem("access", payload.access)
            return {
                ...state,
                isAuthenticated: true,
                access: payload.access,
            }
        default:
            return state


    }
}