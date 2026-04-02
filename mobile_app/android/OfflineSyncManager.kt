package com.obdtechsol.app

import android.content.Context
import org.json.JSONObject
import java.io.File

class OfflineSyncManager(private val context: Context) {

    private val fileName = "offline_queue.json"

    private fun getFile(): File {
        return File(context.filesDir, fileName)
    }

    fun saveOffline(data: JSONObject) {
        val file = getFile()
        file.appendText(data.toString() + "\n")
    }

    fun loadQueue(): List<JSONObject> {
        val file = getFile()
        if (!file.exists()) return emptyList()

        return file.readLines().mapNotNull {
            try { JSONObject(it) } catch (e: Exception) { null }
        }
    }

    fun clearQueue() {
        val file = getFile()
        if (file.exists()) file.delete()
    }
}
