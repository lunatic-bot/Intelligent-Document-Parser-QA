// src/components/ChatBox/ChatBox.view.jsx
function ChatBoxView({ messages, input, setInput, sendMessage }) {
  return (
    <div className="p-4 w-full max-w-2xl mx-auto mt-6">
      <div className="h-80 overflow-y-auto border p-4 rounded bg-gray-50 mb-4">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`mb-2 text-${msg.sender === "user" ? "right" : "left"}`}
          >
            <p
              className={
                msg.sender === "user" ? "text-blue-700" : "text-green-700"
              }
            >
              <strong>{msg.sender === "user" ? "You" : "AI"}:</strong>{" "}
              {msg.text}
            </p>
          </div>
        ))}
      </div>
      <div className="flex">
        <input
          type="text"
          className="border p-2 w-full rounded-l"
          placeholder="Ask a question..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button
          onClick={sendMessage}
          className="bg-blue-500 text-white px-4 rounded-r hover:bg-blue-600"
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default ChatBoxView;
