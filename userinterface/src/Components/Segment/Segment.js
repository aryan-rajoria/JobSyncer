import React from "react";
import Item from "../Item/Item.js";
import "./Segment.css"
export default function Segment (props){
    
    const currPos = props.pos;
    return (
        <div className="segment-list">
            <div className="text-center font-bold text-3xl ">{props.data[currPos]['segment_title'].toUpperCase()}</div>
            {props.data[currPos]['items'].map((section, index) => 
                <div key={index} className="flex flex-col bg-blue-400 my-8 p-6 rounded-lg segment text-white">
                    <span className="font-bold">Title: <input className="font-bold text-lg py-1" type="text" value={section['title']} onChange={event => props.changeTitle(currPos, index, event.target.value)} /></span>
                    <span className="font-bold">Heading: <input className="font-normal italic text-md py-1" type="text" value={section['heading']} onChange={event => props.changeHeading(currPos, index, event.target.value)} /></span>  
                    <span className="font-bold">Description: <input className="font-normal text-sm py-1" type="text" value={section['description']} onChange={event => props.changeDescription(currPos, index, event.target.value)} /></span>
                    {/* <div className="font-bold text-lg">{section['title']}</div>
                    <div className="italic text-md">{section['heading']}</div>
                    <div className="text-sm">{section['description']}</div> */}
                    <p className="font-bold mt-4">Feature List:</p>
                    <Item 
                        features={section['features']} 
                        data={props.data} pos={currPos} 
                        addFeature={props.addFeature} 
                        ind={index} 
                        changeFeature={props.changeFeature}
                    />
                </div>
            )}
        </div>
    );
}