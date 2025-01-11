export default function UploadStatement() {
    
    const upload = () => {

    }
    
    return (
        <div>
            <p className="flex min-h-screen flex-col p-6">
                <span className="bold">Upload a statement</span>
            </p>
            <p>
                <input type="file" id="statement" onChange={upload} />
            </p>

        </div>
    );
}