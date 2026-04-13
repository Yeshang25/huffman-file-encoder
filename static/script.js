// Initialize upload functionality
function initializeUpload(
    formId,
    fileId,
    uploadAreaId,
    fileInfoId,
    fileNameId,
    fileSizeId,
    btnId,
    statusId
) {
    const form = document.getElementById(formId);
    const fileInput = document.getElementById(fileId);
    const uploadArea = document.getElementById(uploadAreaId);
    const fileInfo = document.getElementById(fileInfoId);
    const fileName = document.getElementById(fileNameId);
    const fileSize = document.getElementById(fileSizeId);
    const submitBtn = document.getElementById(btnId);
    const status = document.getElementById(statusId);

    // Drag over
    uploadArea.addEventListener("dragover", (e) => {
        e.preventDefault();
        uploadArea.classList.add("dragover");
    });

    // Drag leave
    uploadArea.addEventListener("dragleave", () => {
        uploadArea.classList.remove("dragover");
    });

    // Drop file
    uploadArea.addEventListener("drop", (e) => {
        e.preventDefault();
        uploadArea.classList.remove("dragover");
        fileInput.files = e.dataTransfer.files;
        handleFileSelect();
    });

    // Click to upload
    uploadArea.addEventListener("click", () => {
        fileInput.click();
    });

    // File selected
    fileInput.addEventListener("change", handleFileSelect);

    function handleFileSelect() {
        const file = fileInput.files[0];
        if (file) {
            fileName.textContent = file.name;
            fileSize.textContent = formatFileSize(file.size);
            fileInfo.classList.add("show");
            submitBtn.disabled = false;

            // Reset status
            status.className = "status";
            status.textContent = "";
        }
    }

    // Form submit (AJAX)
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const formData = new FormData(form);

        try {
            submitBtn.disabled = true;
            submitBtn.textContent = "Processing...";

            const response = await fetch(form.action, {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                throw new Error(await response.text());
            }

            const blob = await response.blob();

            // Create download link
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;

            // File naming
            if (fileId === "compressFile") {
                a.download = "encoded.bin";
            } else {
                a.download = "decoded.txt";
            }

            document.body.appendChild(a);
            a.click();

            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);

            // Success message
            status.className = "status success";
            status.textContent =
                fileId === "compressFile"
                    ? "File encoded successfully!"
                    : "File decoded successfully!";
        } catch (error) {
            status.className = "status error";
            status.textContent = "Error: " + error.message;
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent =
                fileId === "compressFile"
                    ? "Encode File"
                    : "Decode File";
        }
    });
}

// Format file size
function formatFileSize(bytes) {
    if (bytes === 0) return "0 Bytes";
    const k = 1024;
    const sizes = ["Bytes", "KB", "MB", "GB"];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return (
        parseFloat((bytes / Math.pow(k, i)).toFixed(2)) +
        " " +
        sizes[i]
    );
}

// Initialize both forms
initializeUpload(
    "compressForm",
    "compressFile",
    "compressUploadArea",
    "compressFileInfo",
    "compressFileName",
    "compressFileSize",
    "compressBtn",
    "compressStatus"
);

initializeUpload(
    "decompressForm",
    "decompressFile",
    "decompressUploadArea",
    "decompressFileInfo",
    "decompressFileName",
    "decompressFileSize",
    "decompressBtn",
    "decompressStatus"
);