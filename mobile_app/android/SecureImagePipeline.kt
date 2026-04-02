package com.obdtechsol.app

import android.graphics.Bitmap
import java.io.File

class SecureImagePipeline(
    private val camera: SecureCameraManager,
    private val uploader: ImageUploadManager
) {

    fun processAndStore(bitmap: Bitmap, filename: String): File {
        val compressed = uploader.prepareForUpload(bitmap)

        val finalBitmap = android.graphics.BitmapFactory.decodeByteArray(
            compressed, 0, compressed.size
        )

        return camera.savePrivateImage(finalBitmap, filename)
    }

    fun processAndUpload(bitmap: Bitmap, filename: String, uploadFunc: (ByteArray) -> Unit) {
        val data = uploader.prepareForUpload(bitmap)

        try {
            uploadFunc(data)
        } catch (e: Exception) {
            // fallback: store locally if upload fails
            val finalBitmap = android.graphics.BitmapFactory.decodeByteArray(
                data, 0, data.size
            )
            camera.savePrivateImage(finalBitmap, filename)
        }
    }
}
