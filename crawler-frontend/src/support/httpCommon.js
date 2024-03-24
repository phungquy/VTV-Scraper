import axios from "axios";

//const API_VERSION_PREFIX = "/api/v1"

const backend_api = axios.create({
    baseURL: import.meta.env.VITE_CRAWLER_BACKEND_URL,
    headers: {
        Accept: "application/json",
        'Content-Type': 'application/json',
        //'Access-Control-Allow-Origin': '*',
    }
});

export { backend_api }