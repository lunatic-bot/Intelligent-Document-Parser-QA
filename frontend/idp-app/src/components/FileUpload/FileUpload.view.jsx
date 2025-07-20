// src/components/FileUpload/FileUpload.view.jsx
function FileUploadView({
  file,
  uploading,
  error,
  handleFileChange,
  handleUpload,
}) {
  return (
    <div className="p-4 border rounded shadow w-full max-w-md mx-auto mt-8">
      <h2 className="text-xl font-semibold mb-4">Upload a Document</h2>
      <input type="file" onChange={handleFileChange} accept=".pdf,.doc,.txt" />
      {file && <p className="text-sm mt-1">Selected: {file.name}</p>}
      {error && <p className="text-red-500 text-sm mt-2">{error}</p>}
      <button
        onClick={handleUpload}
        disabled={uploading}
        className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        {uploading ? "Uploading..." : "Upload"}
      </button>
    </div>
  );
}

export default FileUploadView;
