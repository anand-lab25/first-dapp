export  default function  WallConnect() {
    return  (
        <div>
            <h2>wallet connection</h2>
            <button onClick={
                () => alert("wallet connected!")
            }>connect wallet</button>
        </div>
    );
}