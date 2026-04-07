import { initializeApp } from "firebase/app";

const firebaseConfig = {
    apiKey: "AIzaSyAyFoMdwHhqY0lKb9RGb3cFSegSrqeCp1w",
    authDomain: "plant-doc-ai.firebaseapp.com",
    projectId: "plant-doc-ai",
    storageBucket: "plant-doc-ai.firebasestorage.app",
    messagingSenderId: "511859488632",
    appId: "1:511859488632:web:7eb280b2aae282a5adba8d",
    measurementId: "G-3464M0BHS7"
};

const app = initializeApp(firebaseConfig);

export default app;