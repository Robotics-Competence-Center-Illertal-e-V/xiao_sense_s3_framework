#include "esp_camera.h"

#define CAMERA_MODEL_XIAO_ESP32S3 // Has PSRAM

#define START_CODE "\xDE\xAD\xBE\xAF"

#include "camera_pins.h"

unsigned long lastCaptureTime = 0; // Last shooting time

inline void set_Y_in_YUV422(camera_fb_t* fb, int x, int y, uint8_t Y)
{
    if (x < 0 || y < 0) return;
    if (x >= fb->width || y >= fb->height) return;
    // Calculate byte offset: 2 bytes per pixel
    int offset = (y * fb->width + x) * 2;
    fb->buf[offset] = Y;
}

inline uint8_t get_Y(camera_fb_t* fb, int x, int y)
{
    if (x < 0 || y < 0) return 0;
    if (x >= fb->width || y >= fb->height)
        return 0;
    int offset = (y * fb->width + x) * 2;
    return fb->buf[offset];
}

inline uint8_t get_U(camera_fb_t* fb, int x, int y)
{
    if (x < 0 || y < 0) return 0;
    if (x >= fb->width || y >= fb->height)
        return 0;
    int pair = (x / 2);  // group of 2 pixels
    int offset = (y * fb->width + pair * 2) * 2;
    return fb->buf[offset + 1];
}

inline uint8_t get_V(camera_fb_t* fb, int x, int y)
{
    if (x < 0 || y < 0) return 0;
    if (x >= fb->width || y >= fb->height)
        return 0;
    int pair = (x / 2);
    int offset = (y * fb->width + pair * 2) * 2;
    return fb->buf[offset + 3];
}

// Save pictures to SD card
void photo_save() {
  // Take a photo
  camera_fb_t *fb = esp_camera_fb_get();

  long U_sum = 0;
  long V_sum = 0;
  int count = 0;
  for(int x = 20; x < 30; x++)
  {
    for(int y = 20; y < 30; y++)
    {
      U_sum += get_U(fb,x,y);
      V_sum += get_V(fb,x,y);
      count ++;
    }
  }

  //send U and V mean to serial
  //Serial.println(String(U_sum/count) + " " +String(V_sum/count));

  // send image to Serial  
  Serial.write(START_CODE, 4);
  Serial.write(fb->buf, fb->len);
  
  // Release image buffer
  esp_camera_fb_return(fb);
}


void setup() {
  Serial.begin(115200);
  while(!Serial); // When the serial monitor is turned on, the program starts to execute

  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.frame_size = FRAMESIZE_96X96;
  config.pixel_format = PIXFORMAT_YUV422; // for streaming
  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
  config.fb_location = CAMERA_FB_IN_PSRAM;
  config.jpeg_quality = 12;
  config.fb_count = 1;
  


  // camera init
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  //diese settings generieren wiederholbare ergebnisse
  sensor_t * s = esp_camera_sensor_get();
  s->set_whitebal(s, 0); //schaltet auto white balance aus.
  s->set_awb_gain(s, 0); //schaltet auto gain aus
  s->set_contrast(s, 2); //setzt kontrast auf maximum
}

void loop() {

    // Get the current time
    unsigned long now = millis();
  
    //take a picture every second
    if ((now - lastCaptureTime) >= 500) {
      photo_save();
      lastCaptureTime = now;
    }
}