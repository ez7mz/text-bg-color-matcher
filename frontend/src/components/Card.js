import React, { useState } from 'react';
import Loader from "./loader/Loader";
import './card.css';

const Card = () => {
    const [response, setResponse] = useState('');

    const sendRequest = async (event) => {
        const msg = event.target.value;
        console.log(msg);

        try {
            const response = await fetch('http://localhost:8000/api/v1/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ msg })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            setResponse(data.message);
        } catch (error) {
            console.error('Error:', error);
        }
    }


    return (
        <div className="card">
            {/* <img src="card-image.jpg" alt="Card" /> */}
            <Loader/>
            <div className="card-content">
                    <input type="text" placeholder="Enter text" name="msg" onChange={sendRequest} />
                    <p>{response}</p>
            </div>
        </div>
    );
};

export default Card;
