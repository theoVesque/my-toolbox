// pages/factorial.tsx
import { useState } from "react";
import axios from "axios";

const FactorialPage = () => {
  const [number, setNumber] = useState<string>("");
  const [result, setResult] = useState<null | number>(null);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      const response = await axios.post("/api/mathematics/factorial", {
        n: parseInt(number),
      });

      setResult(response.data.calculate_factorial);
    } catch (error) {
      console.error("Error calculating factorial", error);
    }
  };

  return (
    <div>
      <h1>Calculate Factorial</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Number:</label>
          <input
            type="number"
            value={number}
            onChange={(e) => setNumber(e.target.value)}
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

export default FactorialPage;
