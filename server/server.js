import express from "express";
import cors from "cors";
import router from "./routes/userRoutes.js";
import historyRouter from "./routes/historyRoutes.js";
import mongoose from "mongoose";
const app = express();
app.use(cors());
app.use(express.json());

app.use("/api", router);
app.use("/", historyRouter);

app.use("/", (req, res) => {
  res.json("welcome");
});
mongoose
  .connect("mongodb+srv://hello:hello@cluster0.jkv1uvj.mongodb.net/medicDB")
  .then(console.log("mongo db Connected"))
  .catch((err) => console.log(err));
app.listen(4000, () => {
  console.log("listening at port --- 4000");
});
