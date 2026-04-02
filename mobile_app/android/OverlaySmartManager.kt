package com.obdtechsol.app

import android.content.Context
import android.os.Handler
import android.os.Looper

class OverlaySmartManager(private val context: Context) {

    private var lastAlertTime = 0L
    private val cooldown = 15000 // 15 sec กัน spam

    fun shouldShowAlert(type: String): Boolean {
        val now = System.currentTimeMillis()

        if (now - lastAlertTime < cooldown) {
            return false
        }

        return when (type) {
            "CRITICAL" -> true
            "WARNING" -> true
            "INFO" -> false
            else -> false
        }
    }

    fun showSmartAlert(message: String, level: String, callback: (String) -> Unit) {
        if (!shouldShowAlert(level)) return

        lastAlertTime = System.currentTimeMillis()

        Handler(Looper.getMainLooper()).post {
            callback(message)
        }
    }
}
