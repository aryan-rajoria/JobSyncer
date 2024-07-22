import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const navigate = useNavigate();
  const [jobUrl, setJobUrl] = useState("");
  function handleInputChange(e){
    setJobUrl(e.target.value);
  }
  async function handleSubmit(e){
    e.preventDefault();
    if(jobUrl === ""){
      alert("Please enter a valid URL");
    }
    else{
      try{
        const res = await fetch("http://localhost:5000/api/process", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ jobUrl }),
        });
        console.log("Success: ", res);
        navigate('/display');

      }
      catch(err){
        console.log("Error in sending URL input !");
      }
    }
  }
  return (
    <div className='bg-indigo-100' style={{height: '100vh' }}>
        <div className="header-2">
      <nav className="bg-white py-2 md:py-4">
        <div className="container px-4 mx-auto md:flex md:items-center">
          <div className="flex justify-between items-center">
            <span href="#" className="font-bold text-xl text-indigo-600" onClick={() => window.open('/')}>JobSyncer</span>
            <button className="border border-solid border-gray-600 px-3 py-1 rounded text-gray-600 opacity-50 hover:opacity-75 md:hidden" id="navbar-toggle">
              <i className="fas fa-bars"></i>
            </button>
          </div>
          <div className="hidden md:flex flex-col md:flex-row md:ml-auto mt-0 md:mt-0" id="navbar-collapse">
            <a href="#" className="p-2 lg:px-4 md:mx-2 text-white rounded bg-indigo-600">Home</a>
            <a href="/signup" className="p-2 lg:px-4 md:mx-2 text-indigo-600 text-center border border-solid border-indigo-600 rounded hover:bg-indigo-600 hover:text-white transition-colors duration-300 mt-1 md:mt-0 md:ml-1">Signup</a>
          </div>
        </div>
      </nav>

      <div className="bg-indigo-100 py-6 md:py-12 flex-grow flex items-center">
        <div className="container px-4 mx-auto">
          <div className="text-center max-w-2xl mx-auto">
            <h1 className="w-2/3 mx-auto text-3xl md:text-4xl font-bold mb-2">Upload your resume bank to get started !! </h1>
            <button className="bg-indigo-600 text-white py-3 px-6 rounded-full text-lg mt-4 font-medium">Upload Here</button>
            <div className="mt-4">
              <img src="//via.placeholder.com/1000x785/fff?text=iMac+Mockup" alt="mockup" className="d-block max-w-full rounded shadow-md" />
            </div>
          </div>

          <div className="text-center max-w-2xl mx-auto mt-16 bg-black rounded-xl text-white px-8 py-12">
            <h1 className="w-2/3 mx-auto text-xl md:text-2xl font-bold mb-2 text-blue-300">Provide Job URL here</h1>
            <div className='flex flex-row items-center justify-evenly bg-gray-1010 mt-10'>
                <input className='bg-white border-solid border-2 border-blue-600 py-3 px-10 rounded-lg shadow-md shadow-blue-700' value={jobUrl} onChange={handleInputChange}/>
                <button className="bg-indigo-600 text-white py-3 px-6 rounded-full text-md font-bold" onClick={handleSubmit}>Submit URL</button>
            </div>
          </div>

          <div className="md:flex md:flex-wrap md:-mx-2 mt-8 md:mt-12">
            <div className="md:w-1/3 md:px-4 xl:px-6 mt-8 md:mt-0 text-center">
              <span className="w-20 border-t-2 border-solid border-indigo-400 inline-block mb-3"></span>
              <h5 className="text-xl font-medium uppercase mb-4">AI-based Suggestions</h5>
            </div>

            <div className="md:w-1/3 md:px-4 xl:px-6 mt-8 md:mt-0 text-center">
              <span className="w-20 border-t-2 border-solid border-indigo-400 inline-block mb-3"></span>
              <h5 className="text-xl font-medium uppercase mb-4">customize as per your job</h5>
            </div>

            <div className="md:w-1/3 md:px-4 xl:px-6 mt-8 md:mt-0 text-center">
              <span className="w-20 border-t-2 border-solid border-indigo-400 inline-block mb-3"></span>
              <h5 className="text-xl font-medium uppercase mb-4">edit with latex without using latex</h5>
            </div>
            {/* <div className='h-[40px] bg-blue-200 w-full'>
                 
            </div> */}
          </div>
        </div>
      </div>
    </div>
    </div>
    
  );
};


