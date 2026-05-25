import {useState}  from  "react";
import {ethers} from "ethers";
export default function WallConnect() {
    const[account, setAccount] = useState(null);
    async function  wallconnect() {
        if(window.ethereum) {
            try {
                const provider =     new  ethers.BrowserProvider(window.ethereum);      
                const accounts =  await providers.send("eth_requestaccounts", []);
                setAccount(accounts[0]);
            } catch(err) {
                console.error("wallet connection failed:", err);
            }
        } else {
            alert("please install metamsk ");
        }
    }
    return  (
        <div style={{textAlign: "center", marginTop: "50px"}}>
        </div>
    )
}