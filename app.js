import db from "./db";
import { collection, getDocs } from "firebase/firestore";

const fetchData = async () => {
    const snapshot = await getDocs(collection(db, "users"));
    snapshot.forEach(doc => {
        console.log(doc.id, doc.data());
    });
};