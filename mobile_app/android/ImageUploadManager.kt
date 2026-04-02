package com.obdtechsol.app

import android.graphics.Bitmap
import java.io.ByteArrayOutputStream

class ImageUploadManager {

    fun compressImage(bitmap: Bitmap, quality: Int = 70): ByteArray {
        val stream = ByteArrayOutputStream()
        bitmap.compress(Bitmap.CompressFormat.JPEG, quality, stream)
        return stream.toByteArray()
    }

    fun resizeBitmap(bitmap: Bitmap, maxWidth: Int = 1024): Bitmap {
        val ratio = bitmap.width.toFloat() / bitmap.height.toFloat()
        val height = (maxWidth / ratio).toInt()
        return Bitmap.createScaledBitmap(bitmap, maxWidth, height, true)
    }

    fun prepareForUpload(bitmap: Bitmap): ByteArray {
        val resized = resizeBitmap(bitmap)
        return compressImage(resized)
    }
}
