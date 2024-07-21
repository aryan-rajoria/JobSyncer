import React, {useState} from "react";
import "./Item.css";
export default function Item(props){
    const [add, setAdd] = useState("");
    const currPos = props.pos;
    const currInd = props.ind;
    function handleInputChange(event){
        setAdd(event.target.value);
    }
    function handleAddFeature(){
        if(add==="") alert("Please enter any value to add to the Feature list");
        else props.addFeature(currPos, currInd, add);
    }
    return (
        <div className="mt-3 relative">
            {/* {props.ind} */}
            {props?.features.map((item, index) => 
                <div key={index} className="item bg-[#2e115a8f] bg-[#7ee8fbb5] rounded-lg my-1 pl-12 py-1 w-1/2 text-gray-900 font-bold">
                    {/* <div>
                        {item}
                    </div> */}
                    <input type="text" value={item} onChange={event => props.changeFeature(currPos, currInd, index, event.target.value)} />
                </div>
            )}
            <div className="flex flex-row items-center justify-between mt-6 ">
                <input 
                    type="text" 
                    val={add} 
                    onChange={handleInputChange}
                    className="border-solid border-black/60 border-[1px] rounded-md py-1 w-1/2  ml-[20px]"
                />
                <div className="add-item" onClick={handleAddFeature}>
                </div>
            </div>
        </div>
    );
}