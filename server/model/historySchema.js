import mongoose from "mongoose";
const historySchema = new mongoose.Schema({
  name: {
    type: String,
    require: true,
  },
  filePath: {
    type: String,
    require: true,
  },
  disease: {
    type: String,
    require: true,
  },
  date: {
    type: Date,
    default: Date.now,
  },
});
export default mongoose.model("History", historySchema);
