import { ChangeEvent } from "react";


export default function Statements() {
    
    const handleUpload = async (event: ChangeEvent<HTMLInputElement>) => {
        console.log("handle upload");

        if (event.target.files) {
            const rawFile = event.target.files.item(0);
            if (rawFile) {
            
                const formData = new FormData()
                formData.append("stmt", event.target.files.item(0));

                const result = await fetch("http://localhost:8000/statements/", {
                    method: "POST",
                    body: formData
                });

                console.log(`Result: ${JSON.stringify(result.body)}`);
            }}
    }
    
    return (
        <div>
            <h1>Statements</h1>
            <div>
                <input type="file" id="fileUpload" onChange={handleUpload} />
                <label htmlFor="fileUpload">Upload a file</label>
            </div>
        </div>
    );
}