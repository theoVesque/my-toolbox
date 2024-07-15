// pages/percent.tsx
import { useState } from "react";
import axios from "axios";

const PercentPage = () => {
  const [value, setValue] = useState("");
  const [percent, setPercent] = useState("");
  const [result, setResult] = useState<null | number>(null);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      const response = await axios.post("/api/mathematics/percent", {
        value: parseFloat(value),
        percent: parseFloat(percent),
      });

      setResult(response.data.calculate_percent);
    } catch (error) {
      console.error("Error calculating percent", error);
    }
  };

  return (
    <div>
      <h1>Calculate Percent</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Percent:</label>
          <input
            type="number"
            value={percent}
            onChange={(e) => setPercent(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Value:</label>
          <input
            type="number"
            value={value}
            onChange={(e) => setValue(e.target.value)}
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

export default PercentPage;
