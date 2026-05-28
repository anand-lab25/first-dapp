"use client";
import {useEffect,useState} from "react";
import {ethers} from "ethers";
export default function Home() {
    const[account, setAccount]= useState(null);
    async function connectWallet(){
        if(window.ethereum) {
            const provider = new ethers.BrowserProvider(window.ethereum);
            const accounts = await provider.send("eth_requestAccounts",[]);
            setAccount(accounts[0]);

        } else {
            alert("Please install Metamask!");
        }
    }
    return(
        <main>
            <h1>Welcome to My First Dapp</h1>
            <button onClick={connectWallet}>ConnectWallet</button>
            {account && <p>connected: {account}</p> }
        </main>
    )
}