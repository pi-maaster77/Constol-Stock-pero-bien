// frontend/src/api/moves.ts

import type { components } from "@/types/api";
import axios from "axios";
import config from "./config.json";

const { apiUrl } = config;

type MovesIn = components["schemas"]["MovesIn"];
type MovesOut = components["schemas"]["MovesOut"];

const paths = {
	movesIn: "/moves/in",
	movesOut: "/moves/out",
};

export const movesIn = async (movesInData: MovesIn[]): Promise<MovesIn[]> => {
	const response = await axios.post(`${apiUrl}${paths.movesIn}`, movesInData);
	return response.data;
};

export const movesOut = async (movesOutData: MovesOut[]): Promise<MovesOut[]> => {
	const response = await axios.post(`${apiUrl}${paths.movesOut}`, movesOutData);
	return response.data;
};