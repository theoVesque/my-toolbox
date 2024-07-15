// pages/median.tsx
import { useState } from "react";
import axios from "axios";

const MedianPage = () => {
  const [values, setValues] = useState<string>("");
  const [result, setResult] = useState<null | number>(null);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    // Convert the comma-separated string into an array of numbers
    const valueArray = values.split(";").map((val) => parseFloat(val.trim()));

    try {
      const response = await axios.post("/api/mathematics/median", {
        value: valueArray,
      });

      setResult(response.data.calculate_median);
    } catch (error) {
      console.error("Error calculating median", error);
    }
  };

  return (
    <div>
      <h1>Calculate Median</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Values (separate with a ;):</label>
          <input
            type="text"
            value={values}
            onChange={(e) => setValues(e.target.value)}
            required
          />
        </div>
        <button type="submit">Calculate</button>
      </form>
      {result !== null && (
        <div>
          <h2>Result: {result}</h2>
        </div>
      )}
    </div>
  );
};

export default MedianPage;
