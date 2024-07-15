// pages/power.tsx
import { useState } from "react";
import axios from "axios";

const PowerPage = () => {
  const [base, setBase] = useState<string>("");
  const [power, setPower] = useState<string>("");
  const [result, setResult] = useState<null | number>(null);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      const response = await axios.post("/api/mathematics/power", {
        base: parseFloat(base),
        power: parseInt(power),
      });

      setResult(response.data.calculate_power);
    } catch (error) {
      console.error("Error calculating power", error);
    }
  };

  return (
    <div>
      <h1>Calculate Power</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Base:</label>
          <input
            type="number"
            value={base}
            onChange={(e) => setBase(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Exponent:</label>
          <input
            type="number"
            value={power}
            onChange={(e) => setPower(e.target.value)}
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

export default PowerPage;
