package com.obdtechsol.app

import android.content.ContentValues
import android.content.Context
import android.graphics.Bitmap
import android.os.Environment
import java.io.File
import java.io.FileOutputStream

class SecureCameraManager(private val context: Context) {

    // Save image to private app storage (not visible in gallery)
    fun savePrivateImage(bitmap: Bitmap, filename: String): File {
        val directory = File(context.filesDir, "secure_images")
        if (!directory.exists()) directory.mkdirs()

        val file = File(directory, filename)
        val output = FileOutputStream(file)
        bitmap.compress(Bitmap.CompressFormat.JPEG, 80, output)
        output.flush()
        output.close()

        return file
    }

    // Optional: save to external but hide from gallery using .nomedia
    fun saveHiddenExternal(bitmap: Bitmap, filename: String): File {
        val directory = File(context.getExternalFilesDir(Environment.DIRECTORY_PICTURES), "hidden_images")
        if (!directory.exists()) directory.mkdirs()

        // create .nomedia
        File(directory, ".nomedia").createNewFile()

        val file = File(directory, filename)
        val output = FileOutputStream(file)
        bitmap.compress(Bitmap.CompressFormat.JPEG, 80, output)
        output.flush()
        output.close()

        return file
    }
}
