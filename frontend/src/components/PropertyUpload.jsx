import { useState } from "react";
import axios from "axios";

function PropertyUpload() {

    const [files, setFiles] = useState([]);
    const [result, setResult] = useState(null);
    const [preview, setPreview] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleUpload = async () => {

    setLoading(true);

    const formData = new FormData();

    for (let i = 0; i < files.length; i++) {
        formData.append("files", files[i]);
    }

    try {

        const response = await axios.post(
            "http://127.0.0.1:8000/pipeline/",
            formData
        );
        console.log("Response received:");
        //console.log(response.data);
        console.log(response.data);   // <-- Add this

        setResult(response.data);
        setLoading(false);
    }catch (error) {

    console.log("FULL ERROR:", error);

    console.log("error.message =", error.message);

    console.log("error.response =", error.response);

    console.log("error.request =", error.request);

    setLoading(false);

}
};
   return (
<div className="container mt-4">

    <h1 className="text-center mb-4">
        🏠 AI Real Estate Platform
    </h1>

    <div className="card p-4 shadow">

        <input
            className="form-control"
            type="file"
            multiple
            onChange={(e) => {
                setFiles(e.target.files);

                if (e.target.files.length > 0) {
                    setPreview(
                        URL.createObjectURL(
                            e.target.files[0]
                        )
                    );
                }
            }}
        />

        <br />

        {preview && (
            <img
                src={preview}
                className="img-fluid rounded"
                width="400"
                alt=""
            />
        )}

        <br />

        <button
            className="btn btn-primary"
            onClick={handleUpload}
        >
            Upload
        </button>

        <br />

        {loading && (
            <h4>Processing Images...</h4>
        )}

    </div>

    <br />

    {
        result &&
        <div className="card p-4 shadow">

            <h2>🏠 Detected Rooms</h2>

            <ul>
                {
                    result.labels.map(
                        (label, index) => (
                            <li key={index}>
                                {label}
                            </li>
                        )
                    )
                }
            </ul>

            <h2>📊 Features</h2>

            <table className="table table-bordered">

                <thead>
                    <tr>
                        <th>Feature</th>
                        <th>Count</th>
                    </tr>
                </thead>

                <tbody>

                    {
                        Object.entries(result.features).map(
                            ([key, value]) => (
                                <tr key={key}>
                                    <td>{key}</td>
                                    <td>{value}</td>
                                </tr>
                            )
                        )
                    }

                </tbody>

            </table>

            <h2 className="text-success">
                💰 ₹ {result.predicted_price}
            </h2>

            <h2>📝 Description</h2>

            <div className="alert alert-info">
                {result.description}
            </div>

            <h2>Advertisement Poster</h2>

                <img
                    src={`http://127.0.0.1:8000/${result.poster}`}
                    width="500"
                    alt="Property Poster"
                />

                <br /><br />

                <a
                    href={`http://127.0.0.1:8000/${result.poster}`}
                    download
                >
                    <button>Download Poster</button>
                </a>

        </div>
    }

</div>
);
}

export default PropertyUpload;
