package com.obdtechsol.app

import android.content.Context

class AuthModeManager(private val context: Context) {

    enum class AuthMode {
        PASSWORD,
        BIOMETRIC,
        FACE
    }

    private var currentMode: AuthMode = AuthMode.PASSWORD

    fun setMode(mode: AuthMode) {
        currentMode = mode
    }

    fun getMode(): AuthMode {
        return currentMode
    }

    fun isBiometricEnabled(): Boolean {
        return currentMode == AuthMode.BIOMETRIC
    }

    fun isFaceEnabled(): Boolean {
        return currentMode == AuthMode.FACE
    }
}
