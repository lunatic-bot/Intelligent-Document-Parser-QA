// src/components/ChatBox/ChatBox.jsx
import { useState } from "react";
import ChatBoxView from "./ChatBox.view";
import axios from "axios";

function ChatBox({ documentId }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);

    try {
      const res = await axios.post("http://localhost:8000/ask", {
        document_id: documentId,
        question: input,
      });

      const aiMsg = { sender: "ai", text: res.data.answer };
      setMessages((prev) => [...prev, aiMsg]);
    } catch {
      setMessages((prev) => [
        ...prev,
        { sender: "ai", text: "Error fetching answer." },
      ]);
    }

    setInput("");
  };

  return ChatBoxView({ messages, input, setInput, sendMessage });
}

export default ChatBox;
