package com.obdtechsol.app

import android.app.Service
import android.content.Intent
import android.graphics.PixelFormat
import android.os.IBinder
import android.view.*
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView

class OverlayProService : Service() {

    private lateinit var windowManager: WindowManager
    private lateinit var view: View

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        windowManager = getSystemService(WINDOW_SERVICE) as WindowManager

        val inflater = LayoutInflater.from(this)
        view = inflater.inflate(R.layout.overlay_pro, null)

        val params = WindowManager.LayoutParams(
            WindowManager.LayoutParams.WRAP_CONTENT,
            WindowManager.LayoutParams.WRAP_CONTENT,
            WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY,
            WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE,
            PixelFormat.TRANSLUCENT
        )

        params.gravity = Gravity.TOP or Gravity.START
        params.x = 0
        params.y = 100

        windowManager.addView(view, params)

        setupDrag(params)
        setupActions()

        return START_STICKY
    }

    private fun setupDrag(params: WindowManager.LayoutParams) {
        var initialX = 0
        var initialY = 0
        var initialTouchX = 0f
        var initialTouchY = 0f

        view.setOnTouchListener { _, event ->
            when (event.action) {
                MotionEvent.ACTION_DOWN -> {
                    initialX = params.x
                    initialY = params.y
                    initialTouchX = event.rawX
                    initialTouchY = event.rawY
                    true
                }
                MotionEvent.ACTION_MOVE -> {
                    params.x = initialX + (event.rawX - initialTouchX).toInt()
                    params.y = initialY + (event.rawY - initialTouchY).toInt()
                    windowManager.updateViewLayout(view, params)
                    true
                }
                else -> false
            }
        }
    }

    private fun setupActions() {
        val status = view.findViewById<TextView>(R.id.status)
        val startBtn = view.findViewById<Button>(R.id.startBtn)
        val reportBtn = view.findViewById<Button>(R.id.reportBtn)

        startBtn.setOnClickListener {
            status.text = "🚀 Job Started"
        }

        reportBtn.setOnClickListener {
            status.text = "📸 Report Sent"
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        if (::view.isInitialized) windowManager.removeView(view)
    }

    override fun onBind(intent: Intent?): IBinder? = null
}
