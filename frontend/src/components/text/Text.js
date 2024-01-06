import React from "react";

const Text = (props) => {
	return (
		<div
			style={{
				backgroundColor: props.bgSelectedColor,
				width: "75%",
				margin: "2rem",
				borderRadius: "1rem",
				padding: "2rem",
				color: props.textSelectedColor,
			}}
		>
			<p
				style={{
					fontSize: "4rem",
					margin: "0",
				}}
			>
				Selected color: {props.bgSelectedColor}
			</p>

			<h2
				style={{
					fontSize: "2rem",
					fontWeight: "bold",
				}}
			>
				Big Title
			</h2>
			<p style={{ fontSize: "1.5rem" }}>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
			<p
				style={{
					fontSize: "1.2rem",
					fontStyle: "italic",
					margin: "0rem",
				}}
			>
				Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
			</p>
			<p
				style={{
					fontSize: "1rem",
					fontWeight: "bold",
					margin: "0rem",
				}}
			>
				Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
			</p>
		</div>
	);
};

export default Text;
