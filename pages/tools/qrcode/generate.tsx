import { useState, ChangeEvent, FormEvent } from "react";
import axios from "axios";
import config from "../../../config";

const GenerateQRCode = () => {
  const [data, setData] = useState<string>("");
  const [color, setColor] = useState<string>("black");
  const [background, setBackground] = useState<string>("white");
  const [logoPath, setLogoPath] = useState<string>("");
  const [size, setSize] = useState<string>("M");
  const [logoPosition, setLogoPosition] = useState<string>("center");
  const [bannerText, setBannerText] = useState<string>("");
  const [bannerPosition, setBannerPosition] = useState<string>("bottom");
  const [bannerBackground, setBannerBackground] = useState<string>("white");
  const [bannerTextColor, setBannerTextColor] = useState<string>("black");
  const [qrCode, setQrCode] = useState<string | null>(null);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    const requestData = {
      data,
      color,
      background,
      logo_path: logoPath,
      size,
      logo_position: logoPosition,
      banner_text: bannerText,
      banner_position: bannerPosition,
      banner_background: bannerBackground,
      banner_text_color: bannerTextColor,
    };

    try {
      const response = await axios.post(
        `${config.apiUrl}/api/qrcode/generate`,
        requestData,
        {
          responseType: "blob", // Important pour recevoir l'image en tant que blob
        }
      );
      const qrCodeUrl = URL.createObjectURL(response.data);
      setQrCode(qrCodeUrl);
    } catch (error) {
      console.error("Error generating QR code:", error);
    }
  };

  return (
    <div>
      <h1>Generate QR Code</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Data: </label>
          <input
            type="text"
            value={data}
            onChange={(e: ChangeEvent<HTMLInputElement>) =>
              setData(e.target.value)
            }
          />
        </div>
        <div>
          <label>Color: </label>
          <input
            type="text"
            value={color}
            onChange={(e: ChangeEvent<HTMLInputElement>) =>
              setColor(e.target.value)
            }
          />
        </div>
        <div>
          <label>Background: </label>
          <input
            type="text"
            value={background}
            onChange={(e: ChangeEvent<HTMLInputElement>) =>
              setBackground(e.target.value)
            }
          />
        </div>
        <div>
          <label>Logo Path: </label>
          <input
            type="text"
            value={logoPath}
            onChange={(e: ChangeEvent<HTMLInputElement>) =>
              setLogoPath(e.target.value)
            }
          />
        </div>
        <div>
          <label>Size: </label>
          <select
            value={size}
            onChange={(e: ChangeEvent<HTMLSelectElement>) =>
              setSize(e.target.value)
            }
          >
            <option value="XS">XS</option>
            <option value="S">S</option>
            <option value="M">M</option>
            <option value="L">L</option>
            <option value="XL">XL</option>
          </select>
        </div>
        <div>
          <label>Logo Position: </label>
          <select
            value={logoPosition}
            onChange={(e: ChangeEvent<HTMLSelectElement>) =>
              setLogoPosition(e.target.value)
            }
          >
            <option value="center">Center</option>
            <option value="top">Top</option>
            <option value="bottom">Bottom</option>
            <option value="left">Left</option>
            <option value="right">Right</option>
          </select>
        </div>
        <div>
          <label>Banner Text: </label>
          <input
            type="text"
            value={bannerText}
            onChange={(e: ChangeEvent<HTMLInputElement>) =>
              setBannerText(e.target.value)
            }
          />
        </div>
        <div>
          <label>Banner Position: </label>
          <select
            value={bannerPosition}
            onChange={(e: ChangeEvent<HTMLSelectElement>) =>
              setBannerPosition(e.target.value)
            }
          >
            <option value="top">Top</option>
            <option value="bottom">Bottom</option>
          </select>
        </div>
        <div>
          <label>Banner Background: </label>
          <input
            type="text"
            value={bannerBackground}
            onChange={(e: ChangeEvent<HTMLInputElement>) =>
              setBannerBackground(e.target.value)
            }
          />
        </div>
        <div>
          <label>Banner Text Color: </label>
          <input
            type="text"
            value={bannerTextColor}
            onChange={(e: ChangeEvent<HTMLInputElement>) =>
              setBannerTextColor(e.target.value)
            }
          />
        </div>
        <button type="submit">Generate QR Code</button>
      </form>
      {qrCode && (
        <div>
          <h2>Generated QR Code</h2>
          <img src={qrCode} alt="Generated QR Code" />
        </div>
      )}
    </div>
  );
};

export default GenerateQRCode;
