import './App.css'
import {React} from 'react';

function App() {

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log('I am uploading')
  }

  return (
    <>
      <div className="sidebar">
        <a className="active" href="#home">Home</a>
        <a href="#news">News</a>
        <a href="#contact">Contact</a>
        <a href="#about">About</a>
      </div>
      <div className="content">
        <form>
          <label>Upload file</label>
          <input type="file" id="statement" />
          <input type="submit" onClick={handleUpload} />
        </form>
      </div>
    </>
  );
}

export default App;
