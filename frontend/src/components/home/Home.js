import React, { useState } from "react";
import Text from "../text/Text";
import SketchPicker from "react-color";
import Loader from "../loader/Loader";

const Home = () => {
  const [bgSelectedColor, setBgSelectedColor] = useState("#000000");
  const [textSelectedColor, setTextSelectedColor] = useState("#ffffff");
  const [response, setResponse] = useState("");

  const handleBgColorChange = async (event) => {
    console.log(event.rgb);
    try {
      const response = await fetch("http://localhost:8000/api/v1/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ color: event.rgb }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();
      setResponse(data.message);
    } catch (error) {
      console.error("Error:", error);
    }
    setBgSelectedColor(event.hex);
  };

  const handleTextColorChange = (color) => {
    setTextSelectedColor(color.hex);
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
      }}
    >
      <Loader />
      <h1
        style={{
          fontSize: "3rem",
          fontWeight: "bold",
          marginBottom: "2rem",
        }}
      >
        Choose a color
      </h1>

      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          gap: "2rem",
        }}
      >
        <img
          src="/imgs/LeftTip.png"
          alt="left-tip"
          style={{ width: "auto", height: "200px" }}
        />

        <SketchPicker
          disableAlpha
          width="200px"
          color={bgSelectedColor}
          onChange={handleBgColorChange}
        />

        <img
          src="/imgs/RightTip.png"
          alt="right-tip"
          style={{ width: "auto", height: "200px" }}
        />
      </div>
      <Text
        bgSelectedColor={bgSelectedColor}
        textSelectedColor={textSelectedColor}
      />
      <img
        src="/imgs/bottomTip.png"
        alt="bottom-tip"
        style={{ width: "auto", height: "200px" }}
      />
    </div>
  );
};

export default Home;
