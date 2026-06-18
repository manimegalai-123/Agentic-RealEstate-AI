import { useEffect, useState } from "react";
import api from "../services/api";

function Home() {

    const [message, setMessage] = useState("");
    const [properties, setProperties] = useState([]);

    const [name, setName] = useState("");
    const [phone, setPhone] = useState("");
    const [purpose, setPurpose] = useState("Buy");

    useEffect(() => {

        api.get("/")
            .then((res) => {
                setMessage(res.data.message);
            });

        api.get("/properties")
            .then((res) => {
                setProperties(res.data);
            })
            .catch((err) => {
                console.log(err);
            });

    }, []);

    // Buyer request
    const sendInterest = async (propertyId) => {

        try {

            const response = await api.post("/interest", {
                property_id: propertyId,
                buyer_name: name,
                phone: phone,
                purpose: purpose
            });

            alert(response.data.message);

        }
        catch (error) {

            console.log(error);
            alert("Failed to send request");

        }
    };

    // Accept poster
    const acceptPoster = async (propertyId) => {

        try {

            const response = await api.post(
                `/poster/accept/${propertyId}`
            );

            alert(response.data.message);

        }
        catch (error) {

            console.log(error);

        }
    };

    // Reject poster
    const rejectPoster = async (propertyId) => {

        try {

            const response = await api.post(
                `/poster/reject/${propertyId}`
            );

            alert(response.data.message);

        }
        catch (error) {

            console.log(error);

        }
    };

    return (
        <>
            <h1>{message}</h1>

            <h2>Available Properties</h2>

            {
                properties.map((property) => (

                    <div
                        key={property.id}
                        style={{
                            border: "1px solid black",
                            padding: "20px",
                            marginBottom: "30px"
                        }}
                    >

                        {/* Poster */}
                        <img
                            src={`http://127.0.0.1:8000/${property.poster}`}
                            width="400"
                            alt="Property"
                        />

                        <h3>₹ {property.price}</h3>

                        <p>{property.description}</p>

                        <br />

                        {/* Download button */}
                        <a
                            href={`http://127.0.0.1:8000/${property.poster}`}
                            download
                        >
                            <button>
                                Download Poster
                            </button>
                        </a>

                        &nbsp;

                        {/* Accept button */}
                        <button
                            onClick={() => acceptPoster(property.id)}
                        >
                            Accept Poster
                        </button>

                        &nbsp;

                        {/* Reject button */}
                        <button
                            onClick={() => rejectPoster(property.id)}
                        >
                            Reject Poster
                        </button>

                        <hr />

                        <h4>Interested in this property?</h4>

                        <input
                            type="text"
                            placeholder="Your Name"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                        />

                        <br /><br />

                        <input
                            type="text"
                            placeholder="Phone Number"
                            value={phone}
                            onChange={(e) => setPhone(e.target.value)}
                        />

                        <br /><br />

                        <select
                            value={purpose}
                            onChange={(e) => setPurpose(e.target.value)}
                        >
                            <option value="Buy">
                                Buy
                            </option>

                            <option value="Rent">
                                Rent
                            </option>

                        </select>

                        <br /><br />

                        <button
                            onClick={() => sendInterest(property.id)}
                        >
                            Send Request
                        </button>

                    </div>

                ))
            }

        </>
    );
}

export default Home;