// frontend/openapi-ts.config.js
export default {
  input: "http://127.0.0.1:8000/openapi.json", // IP directa
  output: "src/types/api.ts",
  inject: "import type { ISODateString } from './ISODatingFormat';\n",
  transform(schemaObject) {
    if (schemaObject.format === "date" || schemaObject.format === "date-time") {
      return "ISODateString";
    }
  },
};