package com.obdtechsol.app

import android.util.Base64
import javax.crypto.Cipher
import javax.crypto.spec.SecretKeySpec

class ImageEncryptionManager {

    private val key = "1234567890123456" // 16-byte key (ควรเปลี่ยนใน production)

    fun encrypt(data: ByteArray): ByteArray {
        val cipher = Cipher.getInstance("AES")
        val secretKey = SecretKeySpec(key.toByteArray(), "AES")
        cipher.init(Cipher.ENCRYPT_MODE, secretKey)
        return cipher.doFinal(data)
    }

    fun decrypt(data: ByteArray): ByteArray {
        val cipher = Cipher.getInstance("AES")
        val secretKey = SecretKeySpec(key.toByteArray(), "AES")
        cipher.init(Cipher.DECRYPT_MODE, secretKey)
        return cipher.doFinal(data)
    }

    fun encryptToBase64(data: ByteArray): String {
        return Base64.encodeToString(encrypt(data), Base64.DEFAULT)
    }

    fun decryptFromBase64(base64: String): ByteArray {
        val decoded = Base64.decode(base64, Base64.DEFAULT)
        return decrypt(decoded)
    }
}
