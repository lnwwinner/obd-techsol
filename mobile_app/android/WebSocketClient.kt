package com.obdtechsol.app

import okhttp3.*
import org.json.JSONObject

class WebSocketClient(private val vehicleId: String) {

    private val client = OkHttpClient()
    private lateinit var ws: WebSocket

    fun connect() {
        val request = Request.Builder()
            .url("ws://10.0.2.2:8000/ws/$vehicleId")
            .build()

        ws = client.newWebSocket(request, object : WebSocketListener() {

            override fun onOpen(webSocket: WebSocket, response: Response) {
                println("Connected to server")
            }

            override fun onMessage(webSocket: WebSocket, text: String) {
                println("Received: $text")

                val json = JSONObject(text)
                val command = json.optString("command")

                handleCommand(command)
            }

            override fun onFailure(webSocket: WebSocket, t: Throwable, response: Response?) {
                println("Error: ${t.message}")
            }
        })
    }

    fun sendStatus(speed: Int, status: String) {
        val json = JSONObject()
        json.put("speed", speed)
        json.put("status", status)

        ws.send(json.toString())
    }

    private fun handleCommand(command: String) {
        when (command) {
            "REDUCE_SPEED" -> println("ลดความเร็ว")
            "FORCE_STOP" -> println("หยุดรถทันที")
        }
    }
}
