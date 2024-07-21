import React, {useState, useEffect} from "react";
import Segment from "../Segment/Segment";
import oldData from "../../data.json";
import "./Display.css";
export default function Display(){
    const [currData, setCurrData] = useState(oldData['data']);
    const [pos, setPos] = useState(0);
    const seg = {
        "segment_title": "",
        "items": [
          {
            "title": "",
            "heading": "",
            "description": "",
            "features": [""]
          }]
    };
    useEffect(() => {
        
    }, [currData]);
    function incrementPos(){
        console.log("increment");
        if(pos !== currData.length-1) setPos(pos+1);
    }
    function decrementPos(){
        if(pos !== 0) setPos(pos-1);
    }
    function addSegment(seg){
        let newData = [...currData];
        let newSeg = seg;
        newData.push(newSeg);
        setCurrData(newData);
        console.log(currData);
    }
    function addFeature(pos, index, str){
        console.log(pos, index, str);
        const newData = [...currData];
        newData[pos]['items'][index]['features'].push(str);
        setCurrData(newData);
    }
    function changeTitle(pos, ind, str){
        const newData = [...currData];
        newData[pos]['items'][ind]['title'] = str;
        setCurrData(newData);
    }
    function changeHeading(pos, ind, str){
        const newData = [...currData];
        newData[pos]['items'][ind]['heading'] = str;
        setCurrData(newData);
    }
    function changeDescription(pos, ind, str){
        const newData = [...currData];
        newData[pos]['items'][ind]['description'] = str;
        setCurrData(newData);
    }
    function changeFeature(pos, ind, num, str){
        const newData = [...currData];
        newData[pos]['items'][ind]['features'][num] = str;
        setCurrData(newData);
    }
    const exportData = () => {
        const jsonString = `data:text/json;chatset=utf-8,${encodeURIComponent(
          JSON.stringify(currData)
        )}`;
        const link = document.createElement("a");
        link.href = jsonString;
        link.download = "data.json";
    
        link.click();
    };
    const createNewFile = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/save-data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ data: currData }),
            });
    
            if (!response.ok) {
                throw new Error('Failed to save file');
            }
    
            const result = await response.text();
            alert(result);
        } catch (error) {
            console.error('Error saving file:', error);
            alert('Error saving file');
        }
    };
    
    return (
        <div className="flex flex-col items-center">
            <div id='view-resume' className="w-[50%] border-solid border-[0.5px] border-gray-400 py-8 px-24 m-8 rounded-lg">
                <div className="view-page">
                    <Segment 
                        pos={pos} 
                        data={currData} 
                        addFeature={addFeature} 
                        addSegment={addSegment} 
                        changeTitle={changeTitle}
                        changeHeading={changeHeading}
                        changeDescription={changeDescription}
                        changeFeature={changeFeature}
                    />
                </div>
                <div id="view_nav" className="flex flex-row items-center justify-between cursor-pointer">
                    <div 
                        className={`relative bg-black w-[6%] aspect-[1] rounded-full cursor-pointer ${pos==0 ? 'view-chng' : ''}`}
                        style={{content: ''}}
                        onClick={decrementPos}
                    >   
                        <div className="triangle-right"></div> 
                    </div>
                    {/* <div className="font-bold">{pos}</div> */}
                    <div 
                        className={`relative bg-black w-[6%] aspect-[1] rounded-full cursor-pointer ${pos==currData.length-1 ? 'view-chng' : ''}`} 
                        style={{content: ''}}
                        onClick={incrementPos}
                    >
                        <div className="triangle-left"></div> 
                    </div>
                </div>
                {/* <div className="add-segment mx-auto my-8" onClick={addSegment}>

                </div> */}
                <div className="flex flex-row items-center justify-center text-center w-[30%] bg-blue-600 rounded-lg border-solid border-blue-900 border-[0.5px] mx-auto my-8 py-4 px-2 font-bold text-gray-100 font-lg cursor-pointer ">
                    Add blank Segment
                </div>
            </div>
            <button onClick={createNewFile} className="bg-fuchsia-900 rounded-lg px-6 py-4 my-4 text-white font-bold">Save Changes</button>
        </div>
    );

}