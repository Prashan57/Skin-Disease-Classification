import { Router } from "express";

import historySchema from "../model/historySchema.js";
const historyRouter = Router();

const historyDataAdd = async (req, res) => {
  const { name, filePath, disease } = req.body;
  console.log(name, filePath, disease);
  if (!name || !filePath || !disease)
    return res
      .status(400)
      .json({ success: false, msg: "Enter Credentials for History" });
  try {
    const historyCreated = await historySchema.create({
      name,
      filePath,
      disease,
    });
  } catch (err) {
    return res.status(400).json({ success: false, msg: "Data not created" });
  }
  return res.status(200).json({ success: true, msg: "Data saved to history" });
};
historyRouter.post("/history", historyDataAdd);

const historyDataRead = async (req, res) => {
  try {
    const historyData = await historySchema.find();
    if (!historyData) {
      return res.status(400).json({ success: false, msg: "No Data Found" });
    }
    return res.status(200).json({ success: true, data: historyData });
  } catch (err) {
    return res.status(400).json({ success: false, msg: "Data not read" });
  }
};
historyRouter.get("/historyData", historyDataRead);

export default historyRouter;
